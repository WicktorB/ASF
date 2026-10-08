"""Generates Word (.docx) and HTML from the Markdown sources.

    python build/build.py                      # templates/, scenarios/*, docs/ → dist/
    python build/build.py scenarios/one-plan-segment templates
    python build/build.py --final path.md      # drop the grey "Guide" boxes (reader version)

Pipeline per file: front-matter → cover block → Mermaid diagrams rendered with mmdc
(kept as code if mmdc is absent) → Pandoc with build/reference.docx → python-docx
post-processing (table headers, dimension colours, header/footer, badges).
Requires: pandoc 3.x, python-docx, pyyaml; optional: @mermaid-js/mermaid-cli (mmdc).
"""
import sys, os, re, json, subprocess, pathlib, shutil, tempfile, hashlib
import yaml
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.table import WD_TABLE_ALIGNMENT

ROOT = pathlib.Path(__file__).resolve().parent.parent
REF = ROOT / "build" / "reference.docx"
DIST = ROOT / "dist"
MMDC = shutil.which("mmdc")

DIM_COLORS = {"D1": "DBEAFE", "D2": "FCE7F3", "D3": "FEF3C7", "D4": "DCFCE7", "D5": "EDE9FE"}
HEAD_FILL = "E5ECE8"
ACCENT = "0E7C4A"
STATUS_COLORS = {"Met": "DCFCE7", "Partly": "FEF3C7", "Not met": "FEE2E2", "Closed": "DCFCE7", "Open": "FEE2E2", "Proposed": "FEF3C7"}

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def split_front_matter(text):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    return (yaml.safe_load(m.group(1)) or {}), text[m.end():]


def cover_block(fm):
    """Meta lines under the title, from the front-matter."""
    lines = []
    def add(label, key):
        v = fm.get(key)
        if v is None: return
        if isinstance(v, list): v = " · ".join(str(x) for x in v)
        if isinstance(v, dict): v = " · ".join(f"{k}: {x}" for k, x in v.items())
        lines.append(f"**{label}** {v}")
    add("Template", "template"); add("Scenario", "scenario"); add("Status", "doc_status"); add("Verdict", "verdict")
    add("Track", "track"); add("Owners", "owners"); add("Filled by", "filled_by"); add("Checked by", "checked_by")
    add("Validated by", "validated_by"); add("Assessed by", "assessed_by"); add("Reviewed by", "reviewed_by")
    add("Discovery step", "discovery_step"); add("Discovery steps", "discovery_steps"); add("Next gate", "next_gate")
    add("Dimensions", "dimensions"); add("Version", "version"); add("Date", "date")
    if not lines: return ""
    return "::: {custom-style=\"Meta\"}\n" + "  \n".join(lines) + "\n:::\n\n"


def render_mermaid(md, workdir):
    """Replace ```mermaid blocks with PNG images when mmdc is available."""
    def repl(m):
        src = m.group(1)
        if not MMDC:
            return "```\n" + src + "\n```"
        h = hashlib.md5(src.encode()).hexdigest()[:8]
        mmd = workdir / f"diag-{h}.mmd"; png = workdir / f"diag-{h}.png"
        mmd.write_text(src)
        cfg = workdir / "mmdc.json"; cfg.write_text('{"theme":"neutral","themeVariables":{"fontFamily":"Arial","fontSize":"14px"}}')
        pp = workdir / "pp.json"
        chrome = os.environ.get("MMDC_CHROME") or shutil.which("chromium") or shutil.which("chromium-browser") or shutil.which("google-chrome")
        if not chrome and pathlib.Path("/opt/pw-browsers/chromium").exists(): chrome = "/opt/pw-browsers/chromium"
        pp.write_text(json.dumps({"args": ["--no-sandbox"], **({"executablePath": chrome} if chrome else {})}))
        try:
            subprocess.run([MMDC, "-i", str(mmd), "-o", str(png), "-b", "white", "-s", "2", "-c", str(cfg), "-p", str(pp)],
                           check=True, capture_output=True, timeout=120)
            return f"![]({png})"
        except Exception as e:  # keep the source visible rather than fail the build
            sys.stderr.write(f"mermaid render failed: {e}\n")
            return "```\n" + src + "\n```"
    return re.sub(r"```mermaid\n(.*?)\n```", repl, md, flags=re.S)


def preprocess(src_path, final=False, workdir=None):
    text = src_path.read_text(encoding="utf-8")
    fm, body = split_front_matter(text)
    title = fm.get("title", src_path.stem)
    body = body.replace("::: {.readme}", "::: {custom-style=\"Readme\"}")
    if final:
        body = re.sub(r"::: \{\.guide\}.*?\n:::\n", "", body, flags=re.S)
    else:
        body = body.replace("::: {.guide}", "::: {custom-style=\"Guide\"}")
    body = render_mermaid(body, workdir)
    md = f"---\ntitle: \"{title}\"\n---\n\n" + cover_block(fm) + body
    return fm, md


def shade_cell(cell, fill):
    tcpr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
    tcpr.append(shd)


TEXT_WIDTH_CM = 17.0


def set_widths(t):
    """Column widths proportional to content length (min 2.4 cm), summing to the text width."""
    ncols = len(t.columns)
    if ncols == 0: return
    lens = [0] * ncols
    for row in t.rows:
        for j, cell in enumerate(row.cells[:ncols]):
            lens[j] = max(lens[j], min(len(cell.text.strip()), 90))
    weights = [max(l, 10) ** 0.75 for l in lens]
    total = sum(weights)
    widths = [max(2.4, TEXT_WIDTH_CM * w / total) for w in weights]
    scale = TEXT_WIDTH_CM / sum(widths)
    widths = [w * scale for w in widths]
    t.autofit = False
    tblpr = t._tbl.tblPr
    layout = OxmlElement("w:tblLayout"); layout.set(qn("w:type"), "fixed"); tblpr.append(layout)
    for row in t.rows:
        for j, cell in enumerate(row.cells[:ncols]):
            cell.width = Cm(widths[j])
    for j, col in enumerate(t.columns):
        col.width = Cm(widths[j])


def postprocess(docx_path, fm):
    doc = Document(str(docx_path))
    # Tables: header row, dimension rows, status cells, keep header with next
    for t in doc.tables:
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_widths(t)
        for i, row in enumerate(t.rows):
            first = row.cells[0].text.strip() if row.cells else ""
            for j, cell in enumerate(row.cells):
                for p in cell.paragraphs:
                    p.paragraph_format.space_after = Pt(2)
                    for r in p.runs:
                        r.font.size = Pt(9)
                if i == 0:
                    shade_cell(cell, HEAD_FILL)
                    for p in cell.paragraphs:
                        for r in p.runs:
                            r.font.bold = True; r.font.color.rgb = RGBColor.from_string(ACCENT)
                    continue
                txt = cell.text.strip()
                if j == 0:
                    key = first[:2]
                    if key in DIM_COLORS and (len(first) < 4 or first[2] in " ·:"):
                        shade_cell(cell, DIM_COLORS[key])
                    for p in cell.paragraphs:
                        for r in p.runs: r.font.bold = True
                key = txt.split(",")[0].strip()
                if key in STATUS_COLORS and len(t.columns) >= 3 and j > 0:
                    shade_cell(cell, STATUS_COLORS[key])
        # repeat header row across pages
        trpr = t.rows[0]._tr.get_or_add_trPr()
        th = OxmlElement("w:tblHeader"); th.set(qn("w:val"), "true"); trpr.append(th)
    # Header and footer
    sec = doc.sections[0]
    sec.different_first_page_header_footer = False
    hdr = sec.header.paragraphs[0] if sec.header.paragraphs else sec.header.add_paragraph()
    hdr.text = f"ASF Design Framework · {fm.get('template', '')} · {fm.get('scenario', '')}".strip(" ·")
    for r in hdr.runs: r.font.size = Pt(8); r.font.color.rgb = RGBColor.from_string("6B7280")
    ftr = sec.footer.paragraphs[0] if sec.footer.paragraphs else sec.footer.add_paragraph()
    ftr.text = f"Generated from the source repository · v{fm.get('version', '')} · {fm.get('date', '')} · do not edit this file: change the Markdown source and rebuild"
    for r in ftr.runs: r.font.size = Pt(7.5); r.font.color.rgb = RGBColor.from_string("9CA3AF")
    doc.save(str(docx_path))


def build_one(src, out_dir, final=False):
    out_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        work = pathlib.Path(td)
        fm, md = preprocess(src, final, work)
        mdfile = work / "in.md"; mdfile.write_text(md, encoding="utf-8")
        stem = src.stem + ("-final" if final else "")
        docx_out = out_dir / f"{stem}.docx"
        subprocess.run(["pandoc", str(mdfile), "-f", "markdown+pipe_tables+fenced_divs+bracketed_spans",
                        "-t", "docx", "--reference-doc", str(REF), "-o", str(docx_out)], check=True)
        postprocess(docx_out, fm)
        html_out = out_dir / f"{stem}.html"
        subprocess.run(["pandoc", str(mdfile), "-f", "markdown+pipe_tables+fenced_divs", "-s", "-t", "html5",
                        "--embed-resources", "--css", str(ROOT / "build" / "html.css"), "-o", str(html_out)], check=True)
    print("built", docx_out.relative_to(ROOT))


def main(argv):
    final = "--final" in argv
    args = [a for a in argv if a != "--final"]
    targets = [ROOT / a for a in args] if args else [ROOT / "templates", ROOT / "scenarios", ROOT / "docs"]
    for t in targets:
        files = [t] if t.is_file() else sorted(t.rglob("*.md"))
        for f in files:
            if f.name.lower() == "readme.md": continue
            rel = f.relative_to(ROOT).parent
            build_one(f, DIST / rel, final)


if __name__ == "__main__":
    main(sys.argv[1:])
