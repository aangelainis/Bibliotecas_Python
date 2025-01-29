import pandas as pd

df = pd.read_csv("Arquivos/titanic.csv")
df.Age = df['Age'].fillna(29.0)
titanic = df[(df['Embarked'] == "S") & (df["Pclass"]== 2) & (df["Age"] == 29.0) & (df["Name"].str.contains("Anne"))]
print(titanic)