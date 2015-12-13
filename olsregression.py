import pandas as pd
import numpy as np
import statsmodels.api as sm
import math

df_adv = pd.read_csv('Draft11.csv', index_col=0)
X = df_adv[["Marital Status - Widowed Females","Marital Status - Separated Persons","Marital Status - Separated Females","Marital Status - Divorced Females","Educational level - Technical diploma or certificate not equal to degree - Persons","Educational level - Technical diploma or certificate not equal to degree - Males","Main Working Population Female","Main Agricultural Labourers Population Female","Main Household Industries Population Female"]]
y = df_adv['Number of Suicides']
df_adv.head()
X = sm.add_constant(X)
est = sm.OLS(y, X).fit()

print est.summary2()
