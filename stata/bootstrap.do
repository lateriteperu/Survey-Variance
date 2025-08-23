* Bootstrap variance example
clear
set obs 100
gen y = rnormal(60,12)

* Bootstrap mean
bootstrap r(mean), reps(200): summarize y
