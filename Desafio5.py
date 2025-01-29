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

qtd_mortes_com_parentes_abordo = df['PassengerId'][(df['SibSp'] != 0) & (df['Survived'] == 0)].count()
print(f'Quantidade de pessoas que morreram com parentes a bordo: {qtd_mortes_com_parentes_abordo}')


###########
# Quantidade das pessoas que morreram sem parentes a bordo

qtd_mortes_sem_parentes_abordo = df['PassengerId'][(df['SibSp'] == 0) & (df['Survived'] == 0)].count()
print(f'Quantidade de pessoas que morreram sem parentes a bordo: {qtd_mortes_sem_parentes_abordo}')


###########
# % de mulheres que morreram

percent_mortes_mulher = ((df['PassengerId'][(df['Sex'] == 'female') & (df['Survived'] == 0)].count()) / pessoas_totais) * 100
print('Porcentagem de mulheres que morreram: {:.2f} %'.format(percent_mortes_mulher))


###########
# % de homens que morreram

percent_mortes_homem = ((df['PassengerId'][(df['Sex'] == 'male') & (df['Survived'] == 0)].count()) / pessoas_totais) * 100
print('Porcentagem de mulheres que morreram: {:.2f} %'.format(percent_mortes_homem))