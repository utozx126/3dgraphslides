.PHONY: build 

TEX_GENERATORS := $(wildcard **/tex.gen.py)
TEX_GENERATED := $(GENERATORS:.gen.py=)

FIGURETEX := $(wildcard anim/*.tex) $(wildcard static/*.tex) $(TEX_GENERATED)
FIGUREPDF := $(FIGURETEX:.tex=.pdf)

default: build

anim/%: anim/%.gen.py
	python3 anim/$*.gen.py > anim/$*

static/%: static/%.gen.py
	python3 static/$*.gen.py > static/$*

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
