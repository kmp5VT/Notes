# maketex_example

Example maketex code for generating literature review in LaTeX. Most files found under /tex. 


maketex is the main script, run this to compile a new pdf. Edit functionality at your own risk.

Body.tex is the main latex file. Configurations are mostly self-explanatory. When compiled with ```./maketex```, it pulls in the tex files for each chapter. Each chapter is a separate tex file- see examples. Chapters included are listed at the bottom of the body.tex file- comment out whichever sections you don't want to include, or rename them to your own chapters. Coversheets are pre-made but not quite correct for 2017 lit review.


Current build will have issues with bibliography, as the references for this example were not available. Replace this with your own .bib file generated with Mendeley etc. and it should work fine.


To compile a new pdf run:
```./maketex body.tex```


To clean irrelevant files(.aux, .bbl, etc) run: 
```./maketex clean```


Result is body.pdf. 


To review only specific sections, comment out (with %) include statements at the end of body.tex and re-compile with maketex.
