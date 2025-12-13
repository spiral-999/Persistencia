import pandas as pd

alunos_df = pd.DataFrame(
    {
        "id": [1,2,3],
        "nome": ["Jefferson", "Wladmir", "Fábio"],
        "curso": ["CC", "SI", "ES"],
        "IRA": [9.7, 4.6, 7.3]
    }
)
print(alunos_df)
print(alunos_df.to_dict(orient="records"))

#obtendo o aluno de id = 2
print(type(alunos_df["id"] == 2))
filtro = alunos_df["id"] == 2
print(alunos_df[filtro])
print(type(alunos_df[filtro]))
print(alunos_df[filtro]["nome"].iloc[0])