# Workflow

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
