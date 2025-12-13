import sys

linha = sys.stdin.readline() # lê a linha a partir do teclado

while linha:
    print("-->" + linha.strip() + "<--") # remove os espaços em branco
    linha = sys.stdin.readline() # pula para a próxima