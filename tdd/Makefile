.PHONY: build 

FIGURETEX := $(wildcard anim/*.tex) $(wildcard static/*.tex)
FIGUREPDF := $(FIGURETEX:.tex=.pdf)

default: build

build: tdd.pdf

preview: $(FIGUREPDF) tdd.tex
	pdflatex --output-directory=build preview.tex
	mv build/preview.pdf .

tdd.pdf: $(FIGUREPDF) tdd.tex 
	latexmk -pdf --output-directory=build tdd.tex
	mv build/tdd.pdf .

static/%.pdf: static/%.tex
	mkdir -p build/static/
	pdflatex -output-directory build/static/ static/$*
	mv build/static/$*.pdf static

anim/%.pdf: anim/%.tex
	mkdir -p build/anim/
	pdflatex -output-directory build/anim/ anim/$*
	mv build/anim/$*.pdf anim
