
## Prototype of a search engine of latex code in scientific articles

Imagine you could search mathematical formulas in scientific articles, it could be useful to search solutions of mathematical problems you're facing and help 
people from different areas to solve different problems using the same math, it also could be used to study the aplications of mathematics in different areas
of science.

In this repo I read 3 different scientific articles and transformed it from pdf to english text and latex code using the pipeline in the repo :  
https://github.com/Gabrielbbe/pdf2img2latex

Then I created a interface to simulate a search engine to search the latex code extracted from the articles.

Example of search : 

![example](https://github.com/Gabrielbbe/Prototype_search_mathematics/assets/104850235/ddb294b6-137e-4d1d-90d8-3a327c016eaa)

Made with streamlit, to run it:
install python, and the packages streamlit, sklearn and pandas p
clone this repo and in the command line where this repo is located type:

'''
streamlit run main.py
'''
