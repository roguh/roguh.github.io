#!/bin/sh
pandoc --highlight-style espresso -s -t slidy intro_to_cs.md -o index.html
# pandoc intro_to_cs.md -o intro_to_cs_by_roguh_2021_11.pdf
