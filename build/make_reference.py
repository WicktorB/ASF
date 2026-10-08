"""Builds build/reference.docx: the Word styles every generated document uses.

Run once (or whenever the styles change):  python build/make_reference.py
Starts from Pandoc's default reference document, then sets fonts, colours,
headings, table style and the custom paragraph styles the templates use
(Readme, Guide, Meta, Badge). Swap the palette for the brand's own values.
"""
import subprocess, pathlib
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = pathlib.Path(__file__).parent
OUT = HERE / "reference.docx"

PALETTE = {
    "ink": "1F2937",        # body text
    "muted": "6B7280",      # meta, guide
    "accent": "0E7C4A",     # headings, band (dark green; brand green 3DCD58 for fills)
    "accent_fill": "3DCD58",
    "readme_bg": "E8F5EC",
    "guide_bg": "F3F4F6",
    "table_head": "E5ECE8",
    "rule": "D1D5DB",
}
FONT = "Arial"

subprocess.run(["pandoc", "-o", str(OUT), "--print-default-data-file", "reference.docx"], check=True)
doc = Document(str(OUT))


class _Styles:
    """Name lookup tolerant to Pandoc's style names (e.g. "Heading 1" stored verbatim)."""
    def __init__(self, st): self.st = st
    def __getitem__(self, name):
        for s in self.st:
            if s.name == name: return s
        return self.st[name]
    def __contains__(self, name): return any(s.name == name for s in self.st)
    def __iter__(self): return iter(self.st)
    def add_style(self, *a, **k): return self.st.add_style(*a, **k)


styles = _Styles(doc.styles)


def set_font(style, size=None, bold=None, italic=None, color=None, name=FONT):
    f = style.font
    f.name = name
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts"); rpr.append(rfonts)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(a), name)
    if size: f.size = Pt(size)
    if bold is not None: f.bold = bold
    if italic is not None: f.italic = italic
    if color: f.color.rgb = RGBColor.from_string(color)


def shade(style, fill):
    ppr = style.element.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
    ppr.append(shd)


def border(style, side, color, sz=12, space=4):
    ppr = style.element.get_or_add_pPr()
    pbdr = ppr.find(qn("w:pBdr"))
    if pbdr is None:
        pbdr = OxmlElement("w:pBdr"); ppr.append(pbdr)
    b = OxmlElement(f"w:{side}")
    b.set(qn("w:val"), "single"); b.set(qn("w:sz"), str(sz)); b.set(qn("w:space"), str(space)); b.set(qn("w:color"), color)
    pbdr.append(b)


def indent(style, left=0.0, right=0.0):
    pf = style.paragraph_format
    pf.left_indent = Cm(left); pf.right_indent = Cm(right)


# Body
normal = styles["Normal"]
set_font(normal, 10, color=PALETTE["ink"])
normal.paragraph_format.space_after = Pt(6)
normal.paragraph_format.line_spacing = 1.15
for name in ("Body Text", "First Paragraph", "Compact"):
    if name in styles:
        set_font(styles[name], 10, color=PALETTE["ink"])

# Title and headings
set_font(styles["Title"], 24, bold=True, color=PALETTE["accent"])
styles["Title"].paragraph_format.space_after = Pt(4)
if "Subtitle" in styles:
    set_font(styles["Subtitle"], 12, color=PALETTE["muted"])
h = styles["Heading 1"]; set_font(h, 17, bold=True, color=PALETTE["accent"])
h.paragraph_format.space_before = Pt(22); h.paragraph_format.space_after = Pt(8)
border(h, "bottom", PALETTE["accent_fill"], sz=12, space=3)
h.paragraph_format.keep_with_next = True
h = styles["Heading 2"]; set_font(h, 13, bold=True, color=PALETTE["ink"])
h.paragraph_format.space_before = Pt(16); h.paragraph_format.space_after = Pt(4); h.paragraph_format.keep_with_next = True
h = styles["Heading 3"]; set_font(h, 11, bold=True, color=PALETTE["accent"])
h.paragraph_format.space_before = Pt(10); h.paragraph_format.space_after = Pt(2); h.paragraph_format.keep_with_next = True
for lvl in (4, 5, 6):
    set_font(styles[f"Heading {lvl}"], 10, bold=True, color=PALETTE["ink"])

# Lists and code
for name in ("Source Code", "Verbatim Char"):
    if name in styles:
        set_font(styles[name], 8.5, name="Consolas")

# Custom paragraph styles used by the templates (pandoc custom-style divs)
readme = styles.add_style("Readme", WD_STYLE_TYPE.PARAGRAPH); readme.base_style = normal
set_font(readme, 9.5, color=PALETTE["ink"]); shade(readme, PALETTE["readme_bg"]); border(readme, "left", PALETTE["accent_fill"], sz=24, space=8)
indent(readme, 0.3, 0.3); readme.paragraph_format.space_before = Pt(6); readme.paragraph_format.space_after = Pt(10)

guide = styles.add_style("Guide", WD_STYLE_TYPE.PARAGRAPH); guide.base_style = normal
set_font(guide, 9, italic=True, color=PALETTE["muted"]); shade(guide, PALETTE["guide_bg"]); indent(guide, 0.3, 0.3)
guide.paragraph_format.space_after = Pt(8)

meta = styles.add_style("Meta", WD_STYLE_TYPE.PARAGRAPH); meta.base_style = normal
set_font(meta, 9, color=PALETTE["muted"]); meta.paragraph_format.space_after = Pt(2)

badge = styles.add_style("Badge", WD_STYLE_TYPE.CHARACTER)
set_font(badge, 9, bold=True, color=PALETTE["accent"])

caption = styles["Caption"] if "Caption" in styles else None
if caption is not None:
    set_font(caption, 8.5, italic=True, color=PALETTE["muted"])

# Table style: light grid, header handled in post-processing
tbl = styles["Table"]
set_font(tbl, 9, color=PALETTE["ink"])
tblpr = tbl.element.find(qn("w:tblPr"))
if tblpr is None:
    tblpr = OxmlElement("w:tblPr"); tbl.element.append(tblpr)
borders = OxmlElement("w:tblBorders")
for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
    b = OxmlElement(f"w:{side}"); b.set(qn("w:val"), "single"); b.set(qn("w:sz"), "4"); b.set(qn("w:space"), "0"); b.set(qn("w:color"), PALETTE["rule"])
    borders.append(b)
tblpr.append(borders)
cellmar = OxmlElement("w:tblCellMar")
for side, w in (("top", 50), ("bottom", 50), ("left", 90), ("right", 90)):
    m = OxmlElement(f"w:{side}"); m.set(qn("w:w"), str(w)); m.set(qn("w:type"), "dxa"); cellmar.append(m)
tblpr.append(cellmar)

# Page: A4, 2 cm margins
for s in doc.sections:
    s.page_width = Cm(21); s.page_height = Cm(29.7)
    s.left_margin = s.right_margin = Cm(2); s.top_margin = Cm(2); s.bottom_margin = Cm(1.8)

doc.save(str(OUT))
print("wrote", OUT)
