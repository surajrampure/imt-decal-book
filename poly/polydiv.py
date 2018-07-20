# polydiv.py

import os
args = os.sys.argv[1:]

div_type = args[0]
dividend = args[1]
divisor = args[2]

latex = "\\documentclass[12pt]{article}" + "\n" + \
"\\pagestyle{empty}" + "\n" + \
"\\usepackage{geometry,hyperref,color,polynom}" + "\n" + \
"\\begin{document}" + "\n"

if div_type == 'l':
	latex += "\polylongdiv{" + dividend + "}{" + divisor + "}" + "\n"
if div_type == 's':
	latex += "\polyhornerscheme[" + divisor + "]{" + dividend + "}" + "\n"

latex += "\\end{document}"

file = open("polydiv.tex", "w")

file.write(latex)
file.close()

os.system('pdflatex polydiv.tex')
os.system('convert -density 300 -trim polydiv.pdf -quality 100 polydiv.png')