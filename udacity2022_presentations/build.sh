#!/bin/sh
# The line above is called the shebang and specifies what program to run this file with

# Read the input from the script's first argument
INPUT_FILE="$(basename "$1")"
INPUT_DIRECTORY="$(dirname "$1")"

# Print all commands before running them. Disable with set +x
set -x

cd "$INPUT_DIRECTORY"

# Create an HTML slideshow using pandoc and a helper library
pandoc --standalone --incremental --slide-level 1 --to slideous "$INPUT_FILE" --output "${INPUT_FILE%.md}.html"

# Create an PDF using latex
# Uncomment the next line to run it
# pandoc --standalone --toc "$INPUT_FILE" --output "${INPUT_FILE%.md}.pdf"
