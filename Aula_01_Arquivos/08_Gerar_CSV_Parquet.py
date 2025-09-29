import pandas as pd

dados = {
    "nome":["Ana", "Bruno", "Carla"],
    "curso":["Matematica", "História", "Física"],
    "notas":["10", "6", "8"]
}

alunos_df = pd.DataFrame(dados)
alunos_df.to_csv("./Aula_01_Arquivos/arquivos/alunos.csv")
alunos_df.to_parquet("./Aula_01_Arquivos/arquivos/alunos.parquet")
