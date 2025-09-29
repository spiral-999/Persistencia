import pandas as pd

df = pd.read_csv("../Persistencia/Aula_03_Pandas/alunos.csv")
print(df)
print(df.head(2))

#retorne um dataframe apenas com os alunos cuja nota > 7
series_bool_aprovados = df["Nota"] > 7
aprovados = df[series_bool_aprovados]
print(aprovados)

notas_organizadas = df.sort_values("Nota", ascending=True)
print(notas_organizadas)