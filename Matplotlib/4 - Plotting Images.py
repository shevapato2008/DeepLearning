import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../largeFiles/train.csv")
df.shape
M = df.as_matrix()
img = M[0, 1:]
img.shape
img = img.reshape(28, 28)                   # change a line to 2-D matrix

plt.imshow(img)

plt.imshow(img, cmap = "gray")              # show in white and black
M[0, 0]                                     # check the label

plt.imshow(255 - img, cmap = "gray")        # show opposite color
