F=*.md

for f in $F
do
  ff="${f%.*}"
  `pandoc --katex -s $f -o $ff.html`
done
