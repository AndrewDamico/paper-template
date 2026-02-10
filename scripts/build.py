import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def ensure_tool(name: str, hint: str) -> None:
    if shutil.which(name) is None:
        print(hint, file=sys.stderr)
        raise SystemExit(1)


def run_convert() -> None:
    print("[1/3] Converting EndNote citations...")
    cmd = [sys.executable, "scripts/convert_citations.py", "--in-dir", "paper/sections", "--out-dir", "paper/generated_md"]
    subprocess.run(cmd, check=True)


def run_pandoc() -> None:
    print("[2/3] Converting Markdown to LaTeX via Pandoc...")
    ensure_tool("pandoc", "Pandoc is required but was not found on PATH.")

    in_dir = Path("paper/generated_md")
    out_dir = Path("paper/generated")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_files = sorted(in_dir.glob("*.md"))
    if not md_files:
        print("No generated Markdown files found. Run the citation conversion step first.", file=sys.stderr)
        raise SystemExit(1)

    for md_file in md_files:
        tex_file = out_dir / (md_file.stem + ".tex")
        cmd = ["pandoc", str(md_file), "-o", str(tex_file)]
        subprocess.run(cmd, check=True)


def run_latexmk(target: str) -> None:
    print(f"[3/3] Building PDF via latexmk + biber (target: {target})...")
    ensure_tool("latexmk", "latexmk is required but was not found on PATH.")
    ensure_tool("biber", "biber is required but was not found on PATH.")

    paper_dir = Path("paper")
    main_file = f"main_{target}.tex"
    cmd = ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "-use-biber", "-outdir=build", main_file]
    subprocess.run(cmd, check=True, cwd=paper_dir)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the paper PDF via Pandoc and latexmk.")
    parser.add_argument("--target", choices=["full", "abstract"], default="full", help="Build target")
    args = parser.parse_args()

    try:
        run_convert()
        run_pandoc()
        run_latexmk(args.target)
    except subprocess.CalledProcessError as exc:
        print(f"Command failed: {exc}", file=sys.stderr)
        return exc.returncode or 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
