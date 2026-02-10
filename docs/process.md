# Workflow

0. Setup: Tooling submodule
   - This template uses a git submodule for shared build scripts.
   - Clone with: git clone --recurse-submodules <repo-url>
   - Or initialize after clone: git submodule update --init --recursive
   - To update tooling: git submodule update --remote --merge
   - Each paper repo pins a specific tooling commit for reproducibility.

1. A) EndNote workflow
   - Maintain one master EndNote library.
   - Create a per-paper Group.
   - Export that Group to BibTeX with keys RN### and save to refs/bibliography.bib.

2. B) Writing workflow
   - Edit paper/sections/*.md in VS Code or Word (as plain text).
   - Keep Markdown headings (#, ##, ###).
   - Insert EndNote unformatted citations like {Bodapati, 2021 #535}.

3. C) Build workflow
   - Run python scripts/build.py --target full or python scripts/build.py --target abstract.
   - It generates paper/generated_md/*.md (citations converted to [@RN###]).
   - It generates paper/generated/*.tex via Pandoc.
   - It compiles paper/main_full.tex or paper/main_abstract.tex via latexmk and biber.
   - Build artifacts are written under paper/build.
   - Build artifacts are not committed.

3.5. Analysis workflow
   1. Put notebooks in code/notebooks and helper scripts in code/src.
   2. In notebooks, import and call bootstrap:
      ```python
      from code.src.bootstrap_tooling import setup_tooling
      setup_tooling()
      import andrewdamico as ad
      ```
   3. Use andrewdamico helpers for run management:
      ```python
      run_id = ad.start_run(label="exp1")
      ad.set_current_run(run_id=run_id)
      ```
   4. When producing figures and tables for the paper, export to paper/figures and paper/tables:
      ```python
      ad.export_figure(name="fig_01", fig=my_fig, formats=["pdf", "png"])
      ad.export_table(name="tbl_01", df=my_df, formats=["tex", "csv"])
      ```
   5. For existing code repositories, add them under code/external/ as submodules:
      ```bash
      git submodule add <url> code/external/<name>
      git submodule update --init --recursive
      ```
   6. Reproducibility: paper repo tags capture the state of paper content + analysis code. The tooling submodule commit is also pinned, ensuring the build and export helpers remain stable.

4. Preserving submissions
   - At submission time, create an annotated tag:
     - git status
     - git add -A
     - git commit -m "Submission vN: <short description>"
     - git tag -a submission-vN -m "Submitted to <venue> on YYYY-MM-DD"
     - git push
     - git push --tags
   - To view a prior submission:
     - git checkout submission-vN
     - python scripts/build.py
   - Reproducibility note: rebuilding later may vary slightly due to toolchain changes. Use GitHub Releases if you need the exact byte-for-byte PDF that was submitted.
   - Submissions are preserved via Git tags and optionally GitHub Releases, not by committing generated PDFs.

5. D) Revision workflow
   - Use revision/roundN/tracker.md to log each reviewer comment, planned fix, file touched, and status.
   - Use response_to_reviewers.md as the final response document.

6. E) Git workflow
   - One section per file.
   - Prefer one person per section at a time.
   - Branch naming conventions (examples): feature/section-intro, fix/typo-lit-review, rev/round1-r1-02.
   - Use PRs and link commits to revision tracker comment IDs.
