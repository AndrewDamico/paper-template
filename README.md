# Academic Paper Template (Markdown + EndNote + Pandoc)

This repository is a reusable template for academic papers authored in Markdown with EndNote unformatted citations. It provides a structured, modular scaffold, a minimal build pipeline, and a LaTeX/PDF output target.

## Prerequisites
- Python 3.x
- Pandoc
- A LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- latexmk
- biber

## Quickstart
Run:

	python scripts/build.py --target full
	python scripts/build.py --target abstract

The default target is full.

## Citation workflow
Write citations in Markdown as {Author, Year #NNN}; export refs/bibliography.bib from EndNote; run the build script; the script converts unformatted citations to [@RN###] and builds the PDF.

## Preserving submissions
Record submissions via Git tags and keep a log in [submissions/SUBMISSIONS.md](submissions/SUBMISSIONS.md). Do not commit generated outputs or PDFs.

## Template vs Generated Files
This repository is intended to be used as a GitHub Template. Generated outputs are ignored. Directories are included via .gitkeep so the structure exists in new repos. Users should not commit PDFs or generated LaTeX unless intentionally creating a tagged submission artifact.

## GitHub template note
This repo is intended to be marked as a GitHub Template in GitHub settings (manual step).
