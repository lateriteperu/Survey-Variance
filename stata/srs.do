* Simple Random Sampling Example
clear
set obs 100
gen y = rnormal(50,10)

* Sample mean and variance (manual)
summarize y

* Variance of mean under SRS
display (r(Var)) / r(N)
