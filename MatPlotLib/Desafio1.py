import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Arquivos/titanic.csv', sep = ",")


###########
# Gráfico de linha

def soma_sibsp_parch(l): # Função de soma de colunas
    return l['SibSp'] + l['Parch']

nova_coluna = df.apply(soma_sibsp_parch, axis = 1)

# plt.plot(df.SibSp.value_counts().sort_index(), color = 'gold', marker = '^', label = 'Número de irmãos/conjuges à bordo')
plt.plot(df.Parch.value_counts().sort_index(), color = 'limegreen', marker = 'o', label = 'Número de filhos/pais à bordo')
# plt.plot(nova_coluna.value_counts().sort_index(), color = 'royalblue', marker = 'x', label = 'Total de parentes à bordo')
plt.legend()
plt.grid(linestyle = 'dashed')
plt.show()

print(nova_coluna)

###########
# Gráfico de barra

x = df.Survived.value_counts().sort_index()
plt.bar(['Not Survived', 'Survived'], x, 0.9, color='red')
plt.legend()
plt.show()
