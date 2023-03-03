#/bin/bash
inkscape -w 128 -h 128 ../refresh.svg -o tmp.png
convert tmp.png -background transparent -gravity center -scale 112x112 -extent 128x128 refresh.png
rm tmp.png
