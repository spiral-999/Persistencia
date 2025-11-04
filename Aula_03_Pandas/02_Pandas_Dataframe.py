import pandas as pd

dados = {
    "Nome":["Ana", "Bruna", "Carlos", "Diana"],
    "Idade":[23,35,45,29],
    "Cidade":["São Paulo", "Fortaleza", "Rio de Janeiro", "Cuiabá"]
}

# --- Criando uma Series a partir de um dicionário
# print(dados["Nome"])
# nome_series = pd.Series(dados["Nome"])
# print (nome_series)

# --- Criando o Dataframe
df = pd.DataFrame(dados)
print(df)

series = pd.Series(df["Idade"])
print(series)
print("Maior Idade : ", df["Idade"].max()) # pega o maximo
print("Maior Idade : ", df["Idade"].min()) # pega o minimo