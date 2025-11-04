# 1. Ler todas as linhas do arquivo. -> lembrar aula 1 de arquivos 
# 2. Separar corretamente as informações de cada aluno.
# 3. Calcular e exibir:
#   ○ A média das notas da turma
#   ○ A maior nota e o nome do aluno que a obteve
#   ○ A menor nota e o nome do aluno que a obteve

notas = []
nomes = []

with open("./Prova/AP1/Questao_01/dados_alunos.txt", "r", encoding="utf-8") as file:
    linha = file.readline()
    while(linha): # 1. Ler todas as linhas do arquivo.
        linha_strip = linha.strip()
        if linha_strip:
            separados = linha_strip.split('#') # 2. Separar corretamente as informações de cada aluno.
            nome_aluno = separados[0] # seguindo o modelo : nome[0], curso[1] -> nao é relevante p questao , nota[2]
            nota_aluno = float(separados[2]) # mudando para float
            #nota_aluno = nota_aluno.astype("float") so funciona com pandas
            notas.append(nota_aluno)
            nomes.append(nome_aluno)
        linha = file.readline()
    
if notas: # se houverem notas -> 3. Calcular e exibir
    print("==============================")
    # ○ A média das notas da turma
    media_turma = sum(notas) / len(notas) # todas as notas / tamanho string
    print(f"A Média da Turma É : {round(media_turma, 2)}") # round() para melhorar a visualização

    print("==============================")
    # ○ A maior nota e o nome do aluno que a obteve
    maior_nota = max(notas) # achando nota
    index_maior = notas.index(maior_nota)
    nome_maior = nomes[index_maior] # achando o aluno
    print(f"A MAIOR Nota foi {maior_nota} e o Aluno foi {nome_maior}")

    print("==============================")
    # ○ A menor nota e o nome do aluno que a obteve
    menor_nota = min(notas) # achando nota
    index_menor = notas.index(menor_nota)
    nome_menor = nomes[index_menor] # achando o aluno
    print(f"A MENOR Nota foi {menor_nota} e o Aluno foi {nome_menor}")
    print("==============================")
