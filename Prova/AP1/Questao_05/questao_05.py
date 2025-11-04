from bs4 import BeautifulSoup

with open("Prova/AP1/Questao_05/jogadas.html", "r", encoding='utf-8') as f:
    soup = BeautifulSoup(f, "html.parser")
    
    tabela = soup.find("table", {"id":"jogadas"})
    linhas = tabela.find_all("tr")[1:] # ignora o cabeçalho

    vitorias_j1 = 0

    for linha in linhas:
        coluna = linha.find_all("td")
        jogada1 = coluna[0].get_text().strip()
        jogada2 = coluna[1].get_text().strip()

        if jogada1 == jogada2:
            continue # se der empate continua
        elif jogada1 == "Pedra" and jogada2 == "Tesoura":
            vitorias_j1 = vitorias_j1 + 1
        elif jogada1 == "Tesoura" and jogada2 == "Papel":
            vitorias_j1 = vitorias_j1 + 1
        elif jogada1 == "Papel" and jogada2 == "Pedra":
            vitorias_j1 = vitorias_j1 + 1

print(f"O Jogador 1 venceu {vitorias_j1} vezes")
