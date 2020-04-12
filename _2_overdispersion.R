#### R code for Crab example
####Poisson Regression Model for Count Data

# https://online.stat.psu.edu/stat504/node/169/

rm(list=ls()) # this clears all variables from the workspace
cat("\014")   # this clears the console
wdir <- "~/repos/count_data/"

setdw(wdir)

crab=read.table("crab.txt")
colnames(crab)=c("Obs","C","S","W","Wt","Sa")

#### to remove the column labeled "Obs"

crab=crab[,-1]

#### Poisson Regression of Sa on W

model=glm(crab$Sa~1+crab$W,family=poisson(link=log))
summary(model)


#### Let's assume for now that we do not have other covariates
#### and we will adjust for overdispersion 
#### first look at the sample mean and variances 
## e.g., tapply(crab$Sa, crab$W,function(x)c(mean=mean(x),variance=var(x)))

#### To estimate dispersion parameter
#### Do it on your own by X2/df & use summary.glm() (see log. reg notes)
#### Use DISMOD package (see log.reg notes)
#### Use quasipoisson family 

model.disp=glm(crab$Sa~crab$W, family=quasipoisson(link=log), data=crab)
summary.glm(model.disp)
summary.glm(model.disp)$dispersion
