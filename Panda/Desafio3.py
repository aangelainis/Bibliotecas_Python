import pandas as pd

df = pd.read_csv("Arquivos/titanic.csv")

# titanic = df[((df["Pclass"] == 1) & (df['Survived'] == 1)) | ((df['Pclass'] == 3) & (df['Survived'] == 0))]
# print(df.head(10))