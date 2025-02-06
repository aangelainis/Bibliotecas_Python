import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Arquivos/respiradores.csv', sep = ",")

# x = df.MES
# y = df.TOTAL
# plt.bar(x, y, 0.9, align='center', color='purple', edgecolor='black')
# plt.title('Compra de Respiradores por Mês')
# plt.xticks(rotation=45)
# plt.yticks(rotation=45)
# plt.xlabel('Meses')
# plt.ylabel('Total por mês')
# plt.show()

# print(help(plt.bar))


# total_por_coluna = df.sum()[1:-1]
# x = df.columns[1:-1]

# plt.bar(x, total_por_coluna, 0.9, color='red', zorder=3) # zorder -> camada, quanto maior mais na frente o elemento aparecerá
# plt.title('Compra de Respiradores por estado')
# plt.xticks(rotation='vertical')
# plt.grid(zorder=0)
# plt.show()


# plt.barh(df.MES, df.TOTAL, color='purple')
# plt.title('Compra de Respiradores por mês')
# plt.show()


###########
#

# plt.plot(df.MES, df.PARANA, color = 'purple', linewidth = 3, marker = 'x') # Gráfico de linha, cor roxa, espessura da linha 3, marcador 'x'
# plt.xticks(rotation = 45) # Rotaciona a legenda de X
# plt.grid(linestyle = 'dashed') # Linhas de grade pontilhadas
# plt.show() # Mostra o gráfico numa nova janela

# print(help(plt.plot)) # Mostra tudo que se pode fazer

###########
# Vários dados num só gráfico

plt.plot(df.MES, df.PARANA, color = 'Purple', marker = 'o', label = 'Paraná')
plt.plot(df.MES, df['SÃO PAULO'], color = 'Red', marker = 'o', label = 'São Paulo')
plt.plot(df.MES, df['SANTA CATARINA'], color = 'Yellow', marker = 'o', label = 'Santa Catarina')
plt.legend() # Habilita a legenda
plt.xticks(rotation = 45)
plt.grid(linestyle = 'dashed')
plt.show()


###########
# Escala - Gráfico de dispersão

# plt.scatter(df['MES'],df['PARANA'], label = 'Paraná')
# plt.scatter(df['MES'],df['SANTA CATARINA'], label = 'Santa Catarina')
# plt.scatter(df['MES'],df['GOIAS'], label = 'Goiás')
# plt.scatter(df['MES'],df['PERNAMBUCO'], label = 'Pernambuco')
# plt.scatter(df['MES'],df['AMAPA'], label = 'Amapá')
# plt.legend() #fontsize=10 / prop={"size":10}
# plt.title("")
# plt.xticks(rotation=45)
# plt.show()


###########
# Vários gráficos

# fig, eixo = plt.subplots(nrows = 2, ncols = 2, figsize = (15, 10))

# eixo[0][0].bar(df.MES, df.TOTAL)
# eixo[0][1].bar(df.columns[1:-1], df.sum()[1:-1])
# eixo[1][0].scatter(df['MES'], df['PARANA'])
# eixo[1][1].plot(df.MES, df.PARANA, color = 'purple')

# plt.show()


###########
# Gráfico de pizza

# estados_sul = df.loc[:, ['PARANA', 'SANTA CATARINA', 'RIO GRANDE DO SUL ']]
# label = estados_sul.columns
# p = estados_sul['PARANA'].sum()
# s = estados_sul['SANTA CATARINA'].sum()
# r = estados_sul['RIO GRANDE DO SUL '].sum()

# print(p, s, r)

# plt.pie([p, s, r], labels = label, autopct = '%.2f%%')
# plt.show()


###########
# Gráfico Histograma 

# total_por_estado = df.iloc[:, 1:-1].sum()
# plt.hist(total_por_estado, rwidth=.9) 
# plt.show()