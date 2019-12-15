#!/bin/sh
DIR=$HOME/sync/nmt/NMT\ CS107/nmt_python_labs/labs/
URL=/tutorials/nmt_python_labs_cs107

tee ../nmt_python_labs_cs107.md << ROGUH
$(cat ../nmt_python_labs_cs107.md.header.yaml)

Carefully written and formatted by a team of students and professors at NMT. See TeX files for attribution.

I rewrote much of the text, assignments, and some of the LaTeX for the 2016 version of the Python labs. This involved testing the assignments and collaborating to write rubrics for them.

Try 'em out!

Contact me at (roguh.com/contact)[https://roguh.com/contact] if you need the supplementary files mentioned in the exercises.

ROGUH

cp "$DIR"/*.{pdf,tex} .
for f in "$DIR"/*.{pdf,tex}; do
  printf "+ [%s](%s)\n" $(basename "$f") $URL/$(basename "$f") >> ../nmt_python_labs_cs107.md
done
