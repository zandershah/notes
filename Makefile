MD_FILES=$(wildcard *.md */*.md)
HTML_FILES=$(MD_FILES:.md=.html)

all: $(HTML_FILES)

# Please let me know if you can do this cleaner.
index.html: index.md
	pandoc --katex --css pandoc.css -s $< -o $@
%.html: %.md
	pandoc --katex --css ../pandoc.css -s $< -o $@
