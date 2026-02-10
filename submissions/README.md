This folder documents submission history in source control, not build artifacts. Source history is in Git commits and tags. Build artifacts are generated outputs and PDFs that can be rebuilt and are not kept in Git history.

Standard practice:
- Tag every submission commit.
- Optionally create a GitHub Release from the tag and upload the exact submitted PDF as a release asset.

We do not commit paper/generated*, paper/build*, or random PDFs because they are overwritten by builds, cause noisy diffs, and do not belong in the source history.

See submissions/SUBMISSIONS.md for the editable log.
