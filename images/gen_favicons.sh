#!/bin/sh
INPUT=hugo_square.svg
convert -resize x16 -gravity center -crop 16x16+0+0 -flatten -colors 256 $INPUT favicon-16x16.ico
convert -resize x32 -gravity center -crop 32x32+0+0 -flatten -colors 256 $INPUT favicon-32x32.ico
convert favicon-16x16.ico favicon-32x32.ico favicon.ico

convert -resize x256 $INPUT favicon-256x256.png
convert -resize x152 $INPUT apple-touch-icon-152x152.png
convert -resize x120 $INPUT apple-touch-icon-120x120.png
convert -resize x76  $INPUT apple-touch-icon-76x76.png
convert -resize x60  $INPUT apple-touch-icon-60x60.png
