* Complex survey design example
clear
set obs 200
gen strata = mod(_n,4)+1
gen cluster = ceil(_n/10)
gen weight = runiform()*2
gen y = rnormal(100,15)

* Declare survey design
svyset cluster [pw=weight], strata(strata)

* Estimate mean with survey design
svy: mean y
