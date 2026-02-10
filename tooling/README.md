# Paper Tooling Submodule

This directory contains the paper-tooling submodule, which provides shared scripts for building academic papers.

## What is tooling/paper-tooling?

The paper-tooling submodule contains:
- Citation conversion scripts (EndNote unformatted -> Pandoc)
- Build orchestration (Markdown -> LaTeX -> PDF via Pandoc and latexmk)
- Shared utilities

Each paper repository pins a specific tooling commit for reproducibility.

## How to initialize

If you cloned without --recurse-submodules:

    git submodule update --init --recursive

## How to update tooling

To get the latest tooling version:

    git submodule update --remote --merge
    git add tooling/paper-tooling
    git commit -m "Update paper-tooling"

## Wrappers

The paper-template repo keeps thin wrapper scripts in scripts/ that delegate to the submodule. This avoids duplicating tooling code across every paper repo.
