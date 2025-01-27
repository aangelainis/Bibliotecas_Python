###########
# Importa a biblioteca

import pandas as pd


###########
# Le o arquivo .csv

# df = pd.read_csv("Arquivos/titanic.csv", sep=",") # df -> data frame


###########
# Retorna a tabela

# print(df.columns[:-1]) # Retorna o nome de todas as colunas, menos a última
# print(df.columns) # Retorna os nomes das colunas
# print(df.iloc[2:, :-1]) # Seleciona o intervalo de colunas e linhas a partir do índice: [Linha, Coluna]
# print(df.loc[200:600, ["Survived"]]) # Seleciona o intervalo de colunas e linhas a partir do índice e do nome: [Linha, Coluna]

############
# Descrição

# print(df.describe()) #descrição
# print(df[['Age', 'Pclass']].describe())

############
# Funções

# print(df["Embarked"].unique()) # A função Unique agrupa valores diferentes da coluna
# print(df.Age.value_counts()) # Igual COUNTDIFF, conta quantos valores iguais tem e os coloca numa tabela


############
# NaN = Not A Number

# df = df.Age.dropna() # Exclui o NaN
# print(df.Age.isna()) # Verifica se é NaN
# df.Age = df.Age.fillna(round(df.Age.mean(), 1)) # Substitui NaN pelo valor dentro dos parênteses, no caso, é a média


# df = df[df["Survived"]==1].sort_values(by = "Age", ascending=False)
# print(df.Age.head())