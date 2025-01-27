import pandas as pd

df = pd.read_csv("BostonHousing.csv", sep=",")

print(df[['crim', 'medv']].head(14)) # =
print(df.loc[0:13, ["crim", "medv"]])