#!/bin/sh
pandoc --highlight-style pygments -s -t slidy intro_to_cs.md -o index.html
pandoc intro_to_cs.md -o intro_to_cs_by_hugo_o_rivera_2021_11.pdf
