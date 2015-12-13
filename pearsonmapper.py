#!/usr/bin/env python
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
import math
import pandas
from pandas import *
import numpy as np
from pydoc import help
from scipy.stats.stats import pearsonr

from sklearn.cross_validation import KFold
corr = []
main=pandas.read_csv("Draft11.csv");
heads=list(main.columns.values)

for i in range(1,70):
	a = main[heads[i]].tolist()
	b = main["Number of Suicides"].tolist()
	c=pearsonr(a, b)
	corr.append(c)
del heads[0]
del heads[69]
for (p,q) in zip(heads,corr):
        if q[0]>0.5:
	  print (p,q)
