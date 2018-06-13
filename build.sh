F=*.md

for f in $F
do
  ff="${f%.*}"
  `pandoc --katex --css pandoc.css -s $f -o $ff.html`
done
