import pandas as pd

# Caso 1 - Erro na formatação esperada
# alunos_dic = {
#    "Nome" : "Jefferson",
#    "Curso" : "SI",
#    "IRA" : 4.5
# }
# Isso gera um erro pois alunos_dic não está formatado
# aluno_df = pd.DataFrame(alunos_dic)
# print(aluno_df)

# Caso 2 - O dev terá que alterar os dados diretamente
# alunos_dic = {
#     "Nome" : ["Jefferson"],
#     "Curso" : ["SI"],
#     "IRA" : [4.5]
# }
# alunos_df = pd.DataFrame(alunos_dic)
# print(alunos_df)

# Caso 3 - Alterando todo o objeto de uma vez
alunos_dic = { # o nome dos campos tem que ser o mesmo para concatenar certo
    "nome" : "Jefferson",
    "curso" : "SI",
    "IRA" : 4.5
}
alunos_df = pd.DataFrame([alunos_dic]) # envolver o dicionário em colchetes
print(alunos_df)

# Persistindo a base de dados
alunos_csv = pd.read_csv("../Persistencia/Aula_04_05_FastAPI/arquivos/alunos.csv")
print(alunos_csv)

# Problema : Persistir o alunos_dic em alunos_csv

# Solução 1 - Concat
alunos_csv = pd.concat([alunos_csv, alunos_df], ignore_index = True) # concat recebe uma lista de dataframes e ignora o novo index
print(alunos_csv)
alunos_csv.to_csv("Aula_04_05_FastAPI/arquivos/alunosNovosConcat.csv", index = False) # cria um csv novo com os dois juntos

print("======================================================================")
# Solução 2 - Append
alunos_csv = alunos_csv._append(alunos_dic, ignore_index = True)
print(alunos_csv)
alunos_csv.to_csv("Aula_04_05_FastAPI/arquivos/alunosNovosAppend.csv", index = False) # cria um csv novo com os dois juntos