# count_data
Links, examples, and code for modelling count data

I am starting this repository as a lose collection of various bits and
pieces around the statistical modelling of count data phenomena. The
purpose is mostly to remind myself of how to do something. I will make
this more organized and add more examples over time. Code is going to
be (mostly) python, but links will be to all sorts of examples.

**LINKS AND READING MATERIAL**

**General**

- [A. Colin Cameron and Pravin K. Trivedi: REGRESSION ANALYSIS OF COUNT
DATA. Second Edition.](http://faculty.econ.ucdavis.edu/faculty/cameron/racd2/) 

- [Regression Models for Count Data in R](https://cran.r-project.org/web/packages/pscl/vignettes/countreg.pdf)

- [Nice Towardsdatascience post on fitting GLMs by hand in python - 
by Daniel Friedman](https://towardsdatascience.com/fitting-glms-by-hand-189c02af33a8)

- [Overdispersion example: Poisson vs NB - by Jeff Meyer](https://www.theanalysisfactor.com/overdispersion-in-count-models-fit-the-model-to-the-data-dont-fit-the-data-to-the-model/)

- [Jay M. Ver Hoef and Peter L. Boveng: QUASI-POISSON VS. NEGATIVE BINOMIAL REGRESSION: HOW SHOULD WE MODEL OVERDISPERSED COUNT DATA? SHOULD WE MODEL OVERDISPERSED COUNT DATA?](https://digitalcommons.unl.edu/cgi/viewcontent.cgi?referer=https://en.wikipedia.org/&httpsredir=1&article=1141&context=usdeptcommercepub)

- [BOOSTEDML: Regression with Count Data: Poisson Regression, Overdispersion, Negative Binomial Regression, and Zero Inflation in R](https://boostedml.com/2019/05/regression-with-count-data-poisson-regression-overdispersion-negative-binomial-regression-and-zero-inflation-in-r.html)

**Poisson Regression**

- [Open `statsmodels` issue on zero-inflated poisson](https://github.com/statsmodels/statsmodels/issues/4952)

- [Open `statsmodels` issue on quasi-poisson. Excellent discussion on connection to robust estimation](https://github.com/statsmodels/statsmodels/issues/4942)

- [Wikipedia article on Poisson regression](https://en.wikipedia.org/wiki/Poisson_regression)

- [Posson Regression Example from UCLA Statistical Consulting](https://stats.idre.ucla.edu/r/dae/poisson-regression/)

- [Stackoverflow: Convergence issues, `statsmodels` vs R](https://stackoverflow.com/questions/21785049/statsmodels-poisson-glm-different-than-r)

- [Stackoverflow: `statsmodels` vs R again, also nice code to get Cook's distance](https://stackoverflow.com/questions/47686227/poisson-regression-in-statsmodels-and-r)

- [Nice Towardsdatascience post on fitting Poisson regression in python - 
by Sachin Date](https://towardsdatascience.com/an-illustrated-guide-to-the-poisson-regression-model-50cccba15958)

- [Sergio Correia, Paulo Guimaraes, and Tom Zylkin: PPMLHDFE: Fast Poisson Estimation withHigh-Dimensional Fixed Effects. Useful, among other things, for clear description of IRLS algorithm in context of Poisson regression](https://arxiv.org/pdf/1903.01690v2.pdf)

- [Another description of IRLS for Python from the gtools documentation](https://gtools.readthedocs.io/en/latest/usage/gpoisson/index.html)

- [Stata manual for fixed effects poisson regression, useful for theory (see "Methods and Formulas")](https://www.stata.com/manuals13/xtxtpoisson.pdf)

- [code snippets from various places on how to implement Poisson regression in `statsmodels` and R](https://code-examples.net/en/q/2d7a253)

- [CrossValidated: Nice Explanation of Overdispersion, zero inflation etc.](https://stats.stackexchange.com/questions/132796/overdispersion-in-poisson-glm)

- [Analysisfactor: Simple example for Poisson regression in R](https://www.theanalysisfactor.com/generalized-linear-models-in-r-part-6-poisson-regression-count-variables/)

**Negative Binomial Regression**

- [Nice Towardsdatascience post on fitting Negative Binommial regression in python - 
by Sachin Date](https://towardsdatascience.com/negative-binomial-regression-f99031bb25b4)





