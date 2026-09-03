"""
Render every slide of a deck to PNG using the installed PowerPoint.

Doubles as quality gate 1: if PowerPoint has to repair the file, Open() fails
or raises here rather than silently succeeding.

    python render.py output/01-ai-general/01-01-ai-fundamentals.pptx preview/AI-01
"""

import os
import shutil
import sys

import win32com.client

PP_ALERTS_NONE = 1


def export(pptx, outdir, width=1920, height=1080):
    pptx = os.path.abspath(pptx)
    outdir = os.path.abspath(outdir)
    if os.path.isdir(outdir):
        shutil.rmtree(outdir)
    os.makedirs(outdir, exist_ok=True)

    app = win32com.client.Dispatch("PowerPoint.Application")
    app.DisplayAlerts = PP_ALERTS_NONE
    pres = None
    try:
        pres = app.Presentations.Open(pptx, ReadOnly=True, WithWindow=False)
        n = pres.Slides.Count
        pres.Export(outdir, "PNG", width, height)
    finally:
        if pres is not None:
            pres.Close()
        try:
            app.Quit()
        except Exception:
            pass
    files = sorted(os.listdir(outdir))
    return n, files


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    n, files = export(src, dst)
    print("%s -> %d slides, %d png" % (os.path.basename(src), n, len(files)))
