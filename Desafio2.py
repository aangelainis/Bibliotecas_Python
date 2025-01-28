# import pandas as pd

# df = pd.read_csv("Arquivos/Cars93_miss.csv", sep = ",")

# # Parte 0
# # print(df.head())
# # print("As opções são: \n")

# # Parte 1
# df = df[df["Passengers"]==5]
# # print(df.head())

# # Parte 2
# df = df.sort_values(by = "MPG.city", ascending=False)
# df = df.head(10)
# # print(df)

# # Parte 3
# df = df.sort_values(by = "Price")
# df = df.head(5)
# # print(df)

# # Parte 4
# df = df.loc[:, ["Manufacturer", "Make", "Price", "MPG.city", "Type", "Passengers"]]
# print(df)