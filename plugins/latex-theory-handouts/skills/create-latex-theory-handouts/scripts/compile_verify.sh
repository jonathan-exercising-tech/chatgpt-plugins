#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 || $# -gt 3 ]]; then
  echo "usage: compile_verify.sh /absolute/path/file.tex [build_dir] [render_dir]" >&2
  exit 2
fi

tex_path="$(realpath "$1")"
if [[ ! -f "$tex_path" ]]; then
  echo "missing TeX source: $tex_path" >&2
  exit 2
fi

source_dir="$(dirname "$tex_path")"
source_name="$(basename "$tex_path")"
base_name="${source_name%.tex}"
build_dir="${2:-$source_dir/build-$base_name}"
render_dir="${3:-$source_dir/rendered-$base_name}"

mkdir -p "$build_dir" "$render_dir"

(
  cd "$source_dir"
  xelatex -interaction=nonstopmode -halt-on-error \
    -output-directory="$build_dir" "$source_name"
  xelatex -interaction=nonstopmode -halt-on-error \
    -output-directory="$build_dir" "$source_name"
)

pdf_path="$build_dir/$base_name.pdf"
log_path="$build_dir/$base_name.log"

test -f "$pdf_path"
pdfinfo "$pdf_path" | grep -E '^(Pages|Page size|File size)'
pdftoppm -png -r 130 "$pdf_path" "$render_dir/$base_name-page"

if grep -nE 'Overfull|LaTeX Warning|Package .* Warning|Missing character' "$log_path"; then
  echo "layout warnings found; inspect the log and rendered pages" >&2
  exit 3
fi

echo "PDF=$pdf_path"
echo "RENDER_DIR=$render_dir"
