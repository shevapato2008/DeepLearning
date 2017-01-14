X = []
import numpy as np
for line in open("data_2d.csv"):
    row = line.split(",")
    sample = map(float, row)
    X.append(sample)

# Continue with 2.1
X = np.array(X)
X.shape

import pandas as pd
X = pd.read_csv("data_2d.csv", header = None)

type(X)
X.info()				# return contents of the dataframe
X.head()				# return first 5 rows
X.head(10)				# you can specify the number of rows to show