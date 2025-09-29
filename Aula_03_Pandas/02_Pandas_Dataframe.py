import pandas as pd

dados = {
    "Nome":["Ana", "Bruna", "Carlos", "Diana"],
    "Idade":[23,35,45,29],
    "Cidade":["São Paulo", "Fortaleza", "Rio de Janeiro", "Cuiabá"]
}

df = pd.DataFrame(dados)
print(df)

series = pd.Series(df["Idade"])
print(series)
print("Maior Idade : ", df["Idade"].max())
print("Maior Idade : ", df["Idade"].min())