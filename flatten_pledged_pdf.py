"""
Resize the tall Pledged PDF to A4 width while keeping all content intact.
Same single tall page — just scaled down to standard width so mobile PDF viewers
render it readable without pinch-to-zoom.
"""

import fitz

BASE = "C:/Users/Femi Fayinminu/OneDrive/Documents/Algolog/Algolog_Projects"
INPUT = f"{BASE}/claude.ai contex/Pledged_MOBILE.pdf"
OUTPUT = f"{BASE}/Proposals/Pledged-Mobile-Outreach.pdf"

src = fitz.open(INPUT)
page = src[0]
src_w = page.rect.width   # 3250
src_h = page.rect.height  # 8449

print(f"Source: {src_w:.0f} x {src_h:.0f}")

# Target width: A4 width (595pt) — keeps aspect ratio
A4_W = 595
scale = A4_W / src_w
new_h = src_h * scale

print(f"Scale: {scale:.4f}")
print(f"Output: {A4_W:.0f} x {new_h:.0f}")

dst = fitz.open()
new_page = dst.new_page(width=A4_W, height=new_h)
new_page.show_pdf_page(fitz.Rect(0, 0, A4_W, new_h), src, 0)

dst.save(OUTPUT, deflate=True, garbage=4)
dst.close()
src.close()

import os
print(f"PDF generated: {OUTPUT}")
print(f"File size: {os.path.getsize(OUTPUT):,} bytes")
