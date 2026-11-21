#!/usr/bin/env python3
"""Konwersja markdown -> PDF (reportlab) bez zewnetrznych zaleznosci."""
import re, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT = "DejaVuSans"
for path in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
             "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"):
    if os.path.exists(path):
        pdfmetrics.registerFont(TTFont(FONT, path)); break
BOLD = FONT

def wrap(text, width, size=9.2):
    lines = []
    for para in text.split("\n"):
        para = re.sub(r"\*\*(.*?)\*\*", r"\1", para)
        para = re.sub(r"`(.*?)`", r"\1", para)
        words = para.split(" ")
        cur = ""
        for w in words:
            t = (cur + " " + w).strip()
            if pdfmetrics.stringWidth(t, FONT, size) > width:
                if cur: lines.append(cur)
                cur = w
            else:
                cur = t
        lines.append(cur)
    return lines

def make(md, pdf, title):
    c = canvas.Canvas(pdf, pagesize=A4)
    w,h = A4
    margin = 18*mm
    y = h - margin
    c.setFont(BOLD, 16); c.drawString(margin, y, title); y -= 12*mm
    c.setFont(FONT, 8); c.drawString(margin, y, "Kiril Kaminskyi | AHE Lodz | AiSD | 21.11.2026"); y -= 9*mm
    text = open(md, encoding="utf-8").read()
    for raw in text.split("\n"):
        raw = raw.rstrip()
        if raw.startswith("|"):
            c.setFont(FONT, 7.6)
            c.drawString(margin, y, re.sub(r"[*|]", " ", raw)[:135]); y -= 4.1*mm
            if y < margin: c.showPage(); y = h - margin
            continue
        sz = 9.2
        if raw.startswith("### "): sz, raw = 12, raw[4:]
        elif raw.startswith("## "): sz, raw = 13, raw[3:]
        elif raw.startswith("# "): sz, raw = 15, raw[2:]
        c.setFont(BOLD if sz>9.2 else FONT, sz)
        for line in wrap(raw, w-2*margin, sz):
            if y < margin:
                c.showPage(); y = h - margin; c.setFont(FONT, sz)
            c.drawString(margin, y, line); y -= sz*mm/6.2 + 2.1*mm
    c.save()
    print("OK", pdf)

B="/home/bokcer/ahe-aisd-coursework"
for name,title in [("C1","AiSD_C1_60 - Proste algorytmy"),
                   ("C2","AiSD_C2_60 - Implementacja prostych algorytmow numerycznych"),
                   ("C3","AiSD_C3_51 - Rekurencja i iteracje")]:
    make(B+"/docs/AiSD_"+name+".md", B+"/docs/AiSD_"+name+".pdf", title)
