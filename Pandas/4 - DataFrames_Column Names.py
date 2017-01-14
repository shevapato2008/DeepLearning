import pandas as pd
df = pd.read_csv("international-airline-passengers.csv", engine="python", skipfooter=3)
df.columns

df.columns = ["months", "passengers"]		# change the column names

df["passengers"]							# return column "passengers"
df.passengers								# equivalent

df['ones'] = 1
df.head()