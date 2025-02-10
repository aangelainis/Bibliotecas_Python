import pandas as pd

df = pd.read_csv("Arquivos/titanic.csv", sep = ",")
pessoas_totais = df['PassengerId'].count()
# print(pessoas_totais)


###########
# % das pessoas que sobreviveram

percent_sobreviventes = ((df['PassengerId'][df["Survived"] == 1].count()) / pessoas_totais) * 100
print('Porcentagem de sobreviventes: {:.2f} %'.format(percent_sobreviventes))


###########
# % das pessoas que sobreviveram
percent_nao_sobreviventes = ((df['PassengerId'][df["Survived"] == 0].count()) / pessoas_totais) * 100
print('Porcentagem de não-sobreviventes: {:.2f} %'.format(percent_nao_sobreviventes))


###########
# % das pessoas que possuiam parentes a bordo

percent_parentes_abordo = ((df['PassengerId'][df['SibSp'] != 0].count()) / pessoas_totais) * 100
print('Porcentagem de pessoas que possuiam parentes a bordo: {:.2f} %'.format(percent_parentes_abordo))


###########
# Quantidade das pessoas que morreram com parentes a bordo

qtd_mortes_com_parentes_abordo = df['PassengerId'][((df['SibSp'] != 0) | (df['Parch'] != 0)) & (df['Survived'] == 0)].count()
print(f'Quantidade de pessoas que morreram com parentes a bordo: {qtd_mortes_com_parentes_abordo}')


###########
# Quantidade das pessoas que morreram sem parentes a bordo

qtd_mortes_sem_parentes_abordo = df['PassengerId'][(df['SibSp'] == 0) & (df['Parch'] == 0) & (df['Survived'] == 0)].count()
print(f'Quantidade de pessoas que morreram sem parentes a bordo: {qtd_mortes_sem_parentes_abordo}')


###########
# % de mulheres que morreram

qtd_mulheres = df['PassengerId'][df['Sex'] == 'female'].count()

percent_mortes_mulher = ((df['PassengerId'][(df['Sex'] == 'female') & (df['Survived'] == 0)].count()) / qtd_mulheres) * 100
print('Porcentagem de mulheres que morreram: {:.2f} %'.format(percent_mortes_mulher))


###########
# % de homens que morreram

qtd_homens = df['PassengerId'][df['Sex'] == 'male'].count()

percent_mortes_homem = ((df['PassengerId'][(df['Sex'] == 'male') & (df['Survived'] == 0)].count()) / qtd_homens) * 100
print('Porcentagem de mulheres que morreram: {:.2f} %'.format(percent_mortes_homem))


###########
# % das pessoas da 1ª classe que morreram

qtd_classe1 = df[df["Pclass"] == 1].shape[0]
percent_mortes_classe1 = (df[(df["Pclass"] == 1) & (df['Survived'] == 0)].shape[0] / qtd_classe1) * 100
print('Porcentagem de pessoas da classe 1 que morreram: {:.2f} %'.format(percent_mortes_classe1))


###########
# % das pessoas da 2ª classe que morreram

qtd_classe2 = df[df["Pclass"] == 2].shape[0]
percent_mortes_classe2 = (df[(df["Pclass"] == 2) & (df['Survived'] == 0)].shape[0] / qtd_classe2) * 100
print('Porcentagem de pessoas da classe 2 que morreram: {:.2f} %'.format(percent_mortes_classe2))


###########
# % das pessoas da 3ª classe que morreram

qtd_classe3 = df[df["Pclass"] == 3].shape[0]
percent_mortes_classe3 = (df[(df["Pclass"] == 3) & (df['Survived'] == 0)].shape[0] / qtd_classe3) * 100
print('Porcentagem de pessoas da classe 3 que morreram: {:.2f} %'.format(percent_mortes_classe3))


###########
# % de crianças que morreram

qtd_criancas = df[(df["Age"] > 0) & (df["Age"] < 12)].shape[0]
percent_mortes_criancas = (df[((df["Age"] > 0) & (df["Age"] < 12)) & (df['Survived'] == 0)].shape[0] / qtd_criancas) * 100
print('Porcentagem de crianças que morreram: {:.2f} %'.format(percent_mortes_criancas))


###########
# % de adolescentes que morreram

qtd_adole = df[(df["Age"] >= 12) & (df["Age"] < 18)].shape[]
percent_mortes_adole = (df[((df["Age"] >= 12) & (df["Age"] < 18)) & (df['Survived'] == 0)].shape[0] / qtd_adole) * 100
print('Porcentagem de adolescentes que morreram: {:.2f} %'.format(percent_mortes_adole))


###########
# % de adultos que morreram

qtd_adultos = df[(df["Age"] >= 18) & (df["Age"] < 60)].shape[0]
percent_mortes_adultos = (df[((df["Age"] >= 18) & (df["Age"] < 60)) & (df['Survived'] == 0)].shape[0] / qtd_adultos) * 100
print('Porcentagem de adultos que morreram: {:.2f} %'.format(percent_mortes_adultos))


###########
# % de idosos que morreram

qtd_idosos = df[(df["Age"] >= 60)].shape[0]
percent_mortes_idosos = (df[(df["Age"] >= 60) & (df['Survived'] == 0)].shape[0] / qtd_idosos) * 100
print('Porcentagem de idosos que morreram: {:.2f} %'.format(percent_mortes_idosos))