X = []
import numpy as np
for line in open("data_2d.csv"):
    row = line.split(",")
    sample = map(float, row)
    X.append(sample)