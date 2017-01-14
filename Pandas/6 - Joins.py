import numpy as np
import pandas as pd

t1 = pd.read_csv('table1.csv')
t2 = pd.read_csv('table2.csv')
t1.head()
t2.head()

m = pd.merge(t1, t2, on = "user_id")
m
t1.merge(t2, on = "user_id")			# equivalent