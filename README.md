# Academic Paper Template (Markdown + EndNote + Pandoc)

This repository is a reusable template for academic papers authored in Markdown with EndNote unformatted citations. It provides a structured, modular scaffold, a minimal build pipeline, and a LaTeX/PDF output target.

## Prerequisites
- Python 3.x
- Pandoc
- A LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- latexmk
- biber

## Cloning and Setup
This template uses a git submodule for shared tooling.

Clone with submodules:

	git clone --recurse-submodules <repo-url>

Or if already cloned, initialize the submodule:

	git submodule update --init --recursive

## Quickstart
Run:

	python scripts/build.py --target full
	python scripts/build.py --target abstract

The default target is full.

## Citation workflow
Write citations in Markdown as {Author, Year #NNN}; export refs/bibliography.bib from EndNote; run the build script; the script converts unformatted citations to [@RN###] and builds the PDF.

## Analysis code (code/)
Analysis code, notebooks, and scripts live in code/.

- code/notebooks: Jupyter notebooks for analysis and experiments
- code/src: Helper scripts and reusable modules
- code/outputs: Scratch outputs (ignored by git)
- code/external: External code repositories as submodules

Final paper-ready figures and tables must be exported to paper/figures and paper/tables using the andrewdamico helpers.

## Using bespoke helpers in notebooks
Notebooks can use the andrewdamico package from the tooling submodule:

```python
from code.src.bootstrap_tooling import setup_tooling
setup_tooling()
import andrewdamico as ad

run_id = ad.start_run(label="exp1")
ad.export_figure(name="my_plot", fig=None, formats=["pdf", "png"])
ad.export_table(name="my_table", df=None, formats=["tex", "csv"])
```

## Using an existing code repository
Add existing code repos as submodules under code/external/ rather than replacing code/:

```bash
git submodule add https://github.com/user/repo code/external/repo
git submodule update --init --recursive
```

Import from external repos in notebooks after running setup_tooling().

## Preserving submissions
Record submissions via Git tags and keep a log in [submissions/SUBMISSIONS.md](submissions/SUBMISSIONS.md). Do not commit generated outputs or PDFs.

## Template vs Generated Files
This repository is intended to be used as a GitHub Template. Generated outputs are ignored. Directories are included via .gitkeep so the structure exists in new repos. Users should not commit PDFs or generated LaTeX unless intentionally creating a tagged submission artifact.

## Tooling Submodule
Build scripts live in a git submodule (tooling/paper-tooling) to avoid duplicating code across paper repos. Each paper pins a specific tooling commit for reproducibility.

To update tooling:

	git submodule update --remote --merge
	git add tooling/paper-tooling
	git commit -m "Update paper-tooling"

## GitHub template note
This repo is intended to be marked as a GitHub Template in GitHub settings (manual step).
