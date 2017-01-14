import pandas as pd
X = pd.read_csv("data_2d.csv", header = None)

# Continue with 2.2
X[0, 0]             # will return error
M = X.as_matrix()   # convert to matrix, but actually returns numpy array
type(M)

M[0]                # Numpy array M[0] returns 0th row
X[0]                # Pandas data frame X[0] will return column that has name 0
type(X[0])
X.iloc[0]           # 0th row for data frame: also a series
X.ix[0]             # equivalent, anything 1 dim in pandas is a series

X[[0, 2]]           # returns column 0 and 2

X[X[0] < 5]
X[0] < 5
type(X[0] < 5)      # returns a list of true and false
