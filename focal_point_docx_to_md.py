# -*- coding: utf-8 -*-
"""Render the Focal Point agreement DOCX to a clean Markdown file for git diffing.

The DOCX (built by generate_focal_point_agreement_final2.py) is the source of
truth for the document that gets sent. This script mirrors its text into
Focal-Point-Agreement.md so wording changes can be reviewed as readable git
diffs. Images (banner, signature) are not text and are represented by their
surrounding labels only.

Run after regenerating the DOCX:
    python generate_focal_point_agreement_final2.py
    python focal_point_docx_to_md.py
"""
import os
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

DOCX = r"C:\Users\Femi Fayinminu\OneDrive\Documents\Proposals_Algolog\Focal_Point\Focal-Point-Agreement-Final-Draft-2.docx"
MD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Focal-Point-Agreement.md")


def iter_block_items(parent):
    body = parent.element.body
    for child in body.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, parent)
        elif child.tag == qn("w:tbl"):
            yield Table(child, parent)


def para_size(p):
    for r in p.runs:
        if r.font.size is not None:
            return r.font.size.pt
    return None


def main():
    doc = Document(DOCX)
    lines = []
    for blk in iter_block_items(doc):
        if isinstance(blk, Table):
            rows = blk.rows
            if not rows:
                continue
            hdr = [c.text.strip().replace("\n", " ") for c in rows[0].cells]
            lines.append("| " + " | ".join(hdr) + " |")
            lines.append("| " + " | ".join(["---"] * len(hdr)) + " |")
            for r in rows[1:]:
                cells = [c.text.strip().replace("\n", " ") for c in r.cells]
                lines.append("| " + " | ".join(cells) + " |")
            lines.append("")
            continue

        p = blk
        text = p.text.strip()
        if not text:
            lines.append("")
            continue

        runs = [r for r in p.runs if r.text]
        allbold = bool(runs) and all(r.bold for r in runs)
        sz = para_size(p)
        style = p.style.name if p.style is not None else ""

        if style == "List Bullet":
            lines.append("- " + text)
        elif sz is not None and sz >= 15:
            lines.append("# " + text)
        elif sz is not None and sz >= 13:
            lines.append("## " + text)
        elif sz is not None and sz >= 12:
            lines.append("### " + text)
        elif allbold:
            lines.append("**" + text + "**")
        else:
            lines.append(text)

    out = "\n".join(lines).strip() + "\n"
    # collapse 3+ blank lines to a single blank line
    while "\n\n\n" in out:
        out = out.replace("\n\n\n", "\n\n")
    with open(MD, "w", encoding="utf-8") as f:
        f.write(out)
    print("Saved:", MD)
    print("Lines:", out.count(chr(10)))


if __name__ == "__main__":
    main()
