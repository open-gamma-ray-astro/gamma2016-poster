TARGET=open-gamma-ray-astro-gamma2016
LATEX=pdflatex
BIBTEX=bibtex

all: $(TARGET).pdf

$(TARGET).pdf: *.tex figures/* text/* $(TARGET).bib

%.pdf: %.tex
	$(LATEX) $<
	$(BIBTEX) $*
	$(LATEX) $<
	$(LATEX) $<

clean:
	- rm -f $(TARGET).pdf $(TARGET).aux $(TARGET).log $(TARGET).bbl $(TARGET).fff
	- rm -f *.aux */*.aux */*/*.aux

tarball:
	- tar -cvzf $(TARGET).tar.gz \
	open-gamma-ray-astro-gamma2016.tex \
	open-gamma-ray-astro-gamma2016.bib \
	text/*.tex \
	figures/purpose.pdf \
	figures/webpage.pdf \
	figures/iact-dl3.pdf \
	figures/dl4-examples.pdf \
	aip-cp.cls aipnum-cp.bst \
	Makefile
