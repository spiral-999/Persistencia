# Fazendo uso do arquivo alunos.csv como um DataFrame, faça:

# 1- Descubra a nota máxima e quem é o aluno com a nota máxima
# 2- Descubra a média das notas e imprima apenas os alunos acima da Média

import pandas as pd

alunos_df = pd.read_csv("../Persistencia/Aula_03_Pandas/arquivos/alunos.csv")

# Aluno com a nota máxima
nota_maxima = alunos_df["Nota"].max()
print("Nota Máxima : ",nota_maxima)
#print(alunos_df["Nota"] == nota_maxima)

alunos_nota_maxima = alunos_df[alunos_df["Nota"] == nota_maxima]
print(alunos_nota_maxima["Nome"])
print("###################################")

# Alunos acima da média
media_notas = alunos_df["Nota"].mean()
print("Média Geral : ", round(media_notas, 2))