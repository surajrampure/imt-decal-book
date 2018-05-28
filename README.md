# imt-decal-book

### Textbook for [Introduction to Mathematical Thinking](http://imt-decal.org), the student run course at UC Berkeley

by Suraj Rampure, with help from others


<br>

The textbook is written in Markdown, and uses [a very handy package](https://www.npmjs.com/package/markdown-folder-to-html) to convert from a Markdown directory to a website, with all links preserved.

- The source Markdown code lives in `src`
- The rendered html lives in `docs`, and this is what GitHub Pages uses to publish the site

To make changes:

1. Ensure `npm` is installed.
2. Run `npm install -g markdown-folder-to-html` to globally install the package on your machine.
3. Clone this repo.
4. Make any changes you want to the `src` folder. Don't do anything to `docs`, as it will be overwritten. Don't touch `CNAME`, or `template.html`. 
5. When done, in the top-level of the folder, run `python3 publish.py` to build the site into `docs`. Run `python3 publish.py -c` if you want to also push your changes to GitHub, making your changes live.