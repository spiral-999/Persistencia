with open("./Aula_01_Arquivos/arquivos/07_escrita.txt", "a", encoding = "utf-8") as file:
    linha = input("Digite o que vai ser escrito no arquivo : ")
    while linha:
        file.write(linha.strip() + "\n")
        linha = input("Digite o que vai ser escrito no arquivo : ")