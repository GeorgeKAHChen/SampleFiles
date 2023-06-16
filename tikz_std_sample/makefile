#Auto Latex Compile
#Copyright by Kazuki Amakawa
#open=explorer.exe   # WSL
#open=xdg-open       # Linux
open=open           # MacOS

filename=main

main: clear
	latex --jobname=${filename} ${filename}.tex
	dvips -o ${filename}.eps ${filename}.dvi
	rm -rf ${filename}.ps
	rm -rf ${filename}.log
	rm -rf ${filename}.aux
	rm -rf ${filename}.out
	rm -rf ${filename}.dvi
	rm -rf ${filename}.bbl
	rm -rf ${filename}.blg
	rm -rf ${filename}.thm
	rm -rf ${filename}.toc
	rm -rf ${filename}.nav
	rm -rf ${filename}.snm

f:full
	echo "f = full"
	
full: main
	open ${filename}.eps

clear:
	rm -rf ${filename}.pdf
	rm -rf ${filename}.eps
	rm -rf ${filename}.ps
	rm -rf ${filename}.log
	rm -rf ${filename}.aux
	rm -rf ${filename}.out
	rm -rf ${filename}.dvi
	rm -rf ${filename}.bbl
	rm -rf ${filename}.blg
	rm -rf ${filename}.thm
	rm -rf ${filename}.toc
	rm -rf ${filename}.nav
	rm -rf ${filename}.snm
