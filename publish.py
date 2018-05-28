import os

os.system("markdown-folder-to-html src")
os.system("mv _src docs")

arg = os.sys.argv[1]

if arg == '-c':
	os.system("git add .")
	os.system("git commit -m 'updating book'")
	os.system("git push")