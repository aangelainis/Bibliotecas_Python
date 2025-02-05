###########
# Importa a biblioteca

import pandas as pd


###########
# Le o arquivo .csv

df = pd.read_csv("Arquivos/titanic.csv", sep=",") # df -> data frame


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


############
# Ordem

# df = df[df["Survived"]==1].sort_values(by = "Age", ascending=False)
# print(df.Age.head())


############
# Filtro

# filtro = df['Pclass'] == 1 # Retorna True e False
# print(df[filtro]) # Retorna dados do filtro


# filtro_apenas_primeira_classe = df[df['Pclass'] == 1] # Retorna dados do filtro
# print(filtro_apenas_primeira_classe)

# print(df[df['Pclass']== 1].head())


############
# Criação de colunas

def soma_sibsp_parch(linha): # Função de soma de colunas
    return linha['SibSp'] + linha['Parch']

nova_coluna = df.apply(soma_sibsp_parch, axis = 1) # Crindo a coluna com valores
df['relatives'] = nova_coluna # Anexando a coluna ao arquivo
df.to_csv('Arquivos/meu_titanic.csv', index = False) # Criando novo arquivo.csv atualizado

print(df)