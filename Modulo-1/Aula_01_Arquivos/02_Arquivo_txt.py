with open("./Aula_01_Arquivos/arquivos/02_alunos.txt", "r") as file:
    linha = file.readline() # lê a primeira linha do arquivo
    print(linha)
    while(linha): 
        print(linha.strip()) # strip() remove os espaços em branco
        linha = file.readline() # pula para a próxima linha
