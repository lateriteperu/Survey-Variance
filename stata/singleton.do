* Example with singleton strata
clear
set obs 50
gen strata = cond(_n<=25,1,2)
gen cluster = _n
gen weight = 1
gen y = rnormal(30,5)

* Stratum 2 has only 1 PSU, causing issues
svyset [pw=weight], psu(cluster) strata(strata) 

* Mean (may trigger single PSU warning)
svy: mean y

* Option: adjust
set svy singleunit(centered)
svy: mean y
