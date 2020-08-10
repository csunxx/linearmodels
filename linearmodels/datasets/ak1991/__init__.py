from pandas import DataFrame

DESCR = """
Angrist and Krueger (1991), "Does Compulsory School Attendance Affect Schooling and Earnings?", Quarterly Journal of Economics (1991)

The data is sourced from Bruce Hansen's website: https://www.ssc.wisc.edu/~bhansen/econometrics/.

There are 329509 observations and 10 features

logwage                  log weekly earnings
edu                      years of education
ageq                     age, including quarter of birth 
married                  =1 if married
black                    =1 if black
region                   region of residence (categorical)
smsa                     1 if the respondent works in a standard metropolitan statistical area, 0 otherwise
yob                      year of birth
state                    state of birth (categorical)
"""


def load() -> DataFrame:
    from linearmodels import datasets

    return datasets.load(__file__, "ak1991.csv.bz2")
