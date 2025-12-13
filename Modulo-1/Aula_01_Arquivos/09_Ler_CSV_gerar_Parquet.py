import pandas as pd
# parquet diminui drasticamente o tamanho do arquivo csv

df = pd.read_csv("./Aula_01_Arquivos/arquivos/alunos.csv")
df.to_parquet("./Aula_01_Arquivos/arquivos/alunos.parquet")