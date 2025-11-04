import pandas as pd # pip install pandas

dados = { # criando o dataframe
    "nome":["Ana", "Bruno", "Carla"],
    "curso":["Matematica", "História", "Física"],
    "notas":["10", "6", "8"]
}

alunos_df = pd.DataFrame(dados) # gerando o dataframe com dados
alunos_df.to_csv("./Aula_01_Arquivos/arquivos/alunos.csv") # to_csv gera o arquivo csv
alunos_df.to_parquet("./Aula_01_Arquivos/arquivos/alunos.parquet") # to_parquet gera o arquivo csv
