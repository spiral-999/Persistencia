import pandas as pd

alunos_df = pd.read_csv("../Persistencia/Aula_03_Pandas/alunos.csv")

# Criar uma nova coluna chamada "Situação"
# Na coluna "Situação", você deve calcular se o aluno foi aprovado ou não(nota>7).
# Se sim, a coluna deve ter valor "Aprovado". Se não, "Reprovado"

def situacao_aluno(nota):
    if nota > 7:
        return "Aprovado"
    elif nota < 4:
        return "Reprovado"
    else:
        return "Recuperação"

alunos_df["Situação"] = alunos_df["Nota"].apply(situacao_aluno) # aplica a função situaçao para cada nota

# Modifique a função para que agora crie:
# A Situação "Aprovado", caso nota > 7
# A Situação "Reprovado", caso nota < 4
# A Situação "Recuperação", caso contrário