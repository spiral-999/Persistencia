import pandas as pd

df = pd.read_csv("../Persistencia/Aula_03_Pandas/arquivos/alunos.csv")
print(df.describe) # dados estatisticos do dataframe
print(df.head(2)) # pega x linhas

# retorne um dataframe apenas com os alunos cuja nota > 7
series_bool_aprovados = df["Nota"] > 7
aprovados = df[series_bool_aprovados]
print(aprovados)

notas_organizadas = df.sort_values("Nota", ascending=True) # organiza de forma "ascendente"
print(notas_organizadas)