import os

os.system("markdown-folder-to-html src")
os.system("rm -rf docs")
os.system("mv _src docs")

if len(os.sys.argv) > 1:
	arg = os.sys.argv[1]

	if arg == '-c':
		os.system("git add .")
		os.system("git commit -m 'updating book'")
		os.system("git push")