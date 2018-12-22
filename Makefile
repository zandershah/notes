MD_FILES=$(wildcard *.md)
HTML_FILES=$(MD_FILES:.md=.html)

all: $(HTML_FILES)

%.html: %.md
	pandoc --katex --css pandoc.css -s $< -o $@
