import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Arquivos/titanic.csv', sep = ',')
# total_parentes = df.SibSp
plt.plot(df.SibSp, df.PassengerId, color = 'Purple', marker = 'o', label = 'Paraná')
plt.plot(df.Parch, df.PassengerId, color = 'Red', marker = 'o', label = 'São Paulo')
plt.legend()
plt.grid(linestyle = 'dashed')
plt.show()
