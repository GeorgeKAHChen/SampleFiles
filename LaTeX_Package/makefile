filename = Chinese

main:
	xelatex ${filename}.tex
	bibtex ${filename}.tex ||true
	xelatex ${filename}.tex
	xelatex ${filename}.tex
	rm -rf ${filename}.{ps,log,aux,out,dvi,bbl,blg,thm,toc}


clear:
	rm -rf ${filename}.pdf
