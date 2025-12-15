import httpx
import random
from datetime import date

# Configuração
BASE_URL = "http://127.0.0.1:8000"

# --- DADOS TEMÁTICOS: COMÉDIA ---

DIRETORES = [
    {"nome": "Todd Phillips", "nacionalidade": "Americano"},       # Se Beber, Não Case
    {"nome": "Judd Apatow", "nacionalidade": "Americano"},         # O Virgem de 40 Anos / Ligeiramente Grávidos
    {"nome": "Adam McKay", "nacionalidade": "Americano"},          # Step Brothers / Anchorman
    {"nome": "Paul Feig", "nacionalidade": "Americano"},           # Missão Madrinha de Casamento / Freaks and Geeks
    {"nome": "Edgar Wright", "nacionalidade": "Britânico"},        # Todo Mundo Quase Morto / Hot Fuzz
    {"nome": "Ivan Reitman", "nacionalidade": "Canadense"},        # Caça-Fantasmas
    {"nome": "Mel Brooks", "nacionalidade": "Americano"},          # O Jovem Frankenstein
    {"nome": "Wes Anderson", "nacionalidade": "Americano"},        # Grande Hotel Budapeste
    {"nome": "Rob Reiner", "nacionalidade": "Americano"},          # A Princesa Prometida / Spinal Tap
    {"nome": "Taika Waititi", "nacionalidade": "Neozelandês"}      # Jojo Rabbit / What We Do in the Shadows
]

ATORES = [
    {"nome": "Steve Carell", "data_nascimento": "1962-08-16"},     # The Office
    {"nome": "Will Ferrell", "data_nascimento": "1967-07-16"},     # Step Brothers
    {"nome": "Seth Rogen", "data_nascimento": "1982-04-15"},       # Ligeiramente Grávidos
    {"nome": "Kristen Wiig", "data_nascimento": "1973-08-22"},     # Missão Madrinha de Casamento
    {"nome": "Simon Pegg", "data_nascimento": "1970-02-14"},       # Hot Fuzz
    {"nome": "Bill Murray", "data_nascimento": "1950-09-21"},      # Caça-Fantasmas
    {"nome": "Gene Wilder", "data_nascimento": "1933-06-11"},      # O Jovem Frankenstein
    {"nome": "Jason Sudeikis", "data_nascimento": "1975-09-18"},   # Ted Lasso
    {"nome": "Andy Samberg", "data_nascimento": "1978-08-18"},     # Brooklyn Nine-Nine
    {"nome": "Tina Fey", "data_nascimento": "1970-05-18"}          # 30 Rock / Meninas Malvadas
]

FILMES = [
    {"titulo": "Se Beber, Não Case!", "ano": 2009, "genero": "Comédia", "nota": 7.7, "diretor_nome": "Todd Phillips"},
    {"titulo": "Ligeiramente Grávidos", "ano": 2007, "genero": "Comédia Romântica", "nota": 6.9, "diretor_nome": "Judd Apatow"},
    {"titulo": "Quase Irmãos", "ano": 2008, "genero": "Comédia", "nota": 6.9, "diretor_nome": "Adam McKay"},
    {"titulo": "Missão Madrinha de Casamento", "ano": 2011, "genero": "Comédia", "nota": 6.8, "diretor_nome": "Paul Feig"},
    {"titulo": "Chumbo Grosso", "ano": 2007, "genero": "Ação/Comédia", "nota": 7.8, "diretor_nome": "Edgar Wright"},
    {"titulo": "Os Caça-Fantasmas", "ano": 1984, "genero": "Sobrenatural/Comédia", "nota": 7.8, "diretor_nome": "Ivan Reitman"},
    {"titulo": "Banzé no Oeste", "ano": 1974, "genero": "Sátira/Western", "nota": 7.7, "diretor_nome": "Mel Brooks"},
    {"titulo": "O Grande Hotel Budapeste", "ano": 2014, "genero": "Comédia/Drama", "nota": 8.1, "diretor_nome": "Wes Anderson"},
    {"titulo": "A Princesa Prometida", "ano": 1987, "genero": "Fantasia/Comédia", "nota": 8.0, "diretor_nome": "Rob Reiner"},
    {"titulo": "O Que Fazemos nas Sombras", "ano": 2014, "genero": "Mockumentary", "nota": 7.7, "diretor_nome": "Taika Waititi"}
]

SERIES = [
    {"titulo": "The Office", "ano_inicio": 2005, "genero": "Mockumentary", "descricao": "Cotidiano de um escritório de papel.", "diretor_nome": "Paul Feig"}, # Dirigiu alguns eps
    {"titulo": "Ted Lasso", "ano_inicio": 2020, "genero": "Esporte/Comédia", "descricao": "Treinador americano na Inglaterra."},
    {"titulo": "Brooklyn Nine-Nine", "ano_inicio": 2013, "genero": "Policial/Comédia", "descricao": "Delegacia de polícia no Brooklyn."},
    {"titulo": "Freaks and Geeks", "ano_inicio": 1999, "genero": "Teen/Comédia", "descricao": "Vida no ensino médio nos anos 80.", "diretor_nome": "Paul Feig"},
    {"titulo": "Parks and Recreation", "ano_inicio": 2009, "genero": "Mockumentary", "descricao": "Departamento de parques em Indiana."},
    {"titulo": "30 Rock", "ano_inicio": 2006, "genero": "Sátira", "descricao": "Bastidores de um programa de TV."},
    {"titulo": "Community", "ano_inicio": 2009, "genero": "Sitcom", "descricao": "Grupo de estudos em faculdade comunitária."},
    {"titulo": "Seinfeld", "ano_inicio": 1989, "genero": "Sitcom", "descricao": "Show sobre nada."},
    {"titulo": "Arrested Development", "ano_inicio": 2003, "genero": "Sitcom", "descricao": "Família rica que perdeu tudo."},
    {"titulo": "What We Do in the Shadows", "ano_inicio": 2019, "genero": "Terror/Comédia", "descricao": "Vampiros dividindo casa em Staten Island.", "diretor_nome": "Taika Waititi"}
]

# Associações específicas (Nome Ator -> Título da Obra) para garantir realismo
ASSOCIACOES_ESPECIFICAS = [
    ("Steve Carell", "The Office"),
    ("Steve Carell", "O Âncora: A Lenda de Ron Burgundy"), # Se estivesse na lista, mas vamos tentar associar a outro do Adam McKay se der
    ("Will Ferrell", "Quase Irmãos"),
    ("Will Ferrell", "The Office"), # Participação especial
    ("Seth Rogen", "Ligeiramente Grávidos"),
    ("Seth Rogen", "Freaks and Geeks"),
    ("Kristen Wiig", "Missão Madrinha de Casamento"),
    ("Simon Pegg", "Chumbo Grosso"),
    ("Bill Murray", "Os Caça-Fantasmas"),
    ("Bill Murray", "O Grande Hotel Budapeste"),
    ("Gene Wilder", "Banzé no Oeste"), # Mel Brooks connection
    ("Jason Sudeikis", "Ted Lasso"),
    ("Andy Samberg", "Brooklyn Nine-Nine"),
    ("Tina Fey", "30 Rock"),
    ("Paul Rudd", "O Âncora") # Exemplo se adicionarmos
]

def log(msg, tipo="INFO"):
    cores = {"INFO": "\033[94m", "SUCESSO": "\033[92m", "ERRO": "\033[91m", "RESET": "\033[0m"}
    print(f"{cores.get(tipo, '')}[{tipo}] {msg}{cores['RESET']}")

def run():
    client = httpx.Client(base_url=BASE_URL, timeout=15.0)
    
    # Mapas para guardar IDs gerados { "Nome": ID }
    mapa_diretores = {}
    mapa_atores = {}
    mapa_filmes = {}
    mapa_series = {}

    log("=== INICIANDO POVOAMENTO DO BANCO DE DADOS (TEMA: COMÉDIA) ===")

    # 1. CRIAR DIRETORES
    print("\n--- Criando Diretores ---")
    for d in DIRETORES:
        resp = client.post("/diretores/", json=d)
        if resp.status_code == 201:
            data = resp.json()
            mapa_diretores[data["nome"]] = data["id"]
            log(f"Diretor criado: {data['nome']} (ID: {data['id']})", "SUCESSO")
        else:
            log(f"Falha ao criar diretor {d['nome']}: {resp.text}", "ERRO")

    # 2. CRIAR ATORES
    print("\n--- Criando Atores ---")
    for a in ATORES:
        resp = client.post("/atores/", json=a)
        if resp.status_code == 201:
            data = resp.json()
            mapa_atores[data["nome"]] = data["id"]
            log(f"Ator criado: {data['nome']} (ID: {data['id']})", "SUCESSO")
        else:
            log(f"Falha ao criar ator {a['nome']}: {resp.text}", "ERRO")

    # 3. CRIAR FILMES
    print("\n--- Criando Filmes ---")
    for f in FILMES:
        nome_dir = f.pop("diretor_nome", None)
        diretor_id = mapa_diretores.get(nome_dir)
        
        # Se não achar o diretor específico, pega um aleatório
        if not diretor_id:
            diretor_id = random.choice(list(mapa_diretores.values())) if mapa_diretores else None
        
        f["diretor_id"] = diretor_id
        
        resp = client.post("/filmes/", json=f)
        if resp.status_code == 201:
            data = resp.json()
            mapa_filmes[data["titulo"]] = data["id"]
            log(f"Filme criado: {data['titulo']} (ID: {data['id']})", "SUCESSO")
        else:
            log(f"Falha ao criar filme {f['titulo']}: {resp.text}", "ERRO")

    # 4. CRIAR SÉRIES + EPISÓDIOS
    print("\n--- Criando Séries ---")
    for s in SERIES:
        nome_dir = s.pop("diretor_nome", None)
        diretor_id = mapa_diretores.get(nome_dir)
        
        if not diretor_id:
            diretor_id = random.choice(list(mapa_diretores.values())) if mapa_diretores else None
            
        s["diretor_id"] = diretor_id
        
        resp = client.post("/series/", json=s)
        if resp.status_code == 201:
            data = resp.json()
            serie_id = data["id"]
            mapa_series[data["titulo"]] = serie_id
            log(f"Série criada: {data['titulo']} (ID: {serie_id})", "SUCESSO")
            
            # Criar 3 Episódios para cada série
            for ep_num in range(1, 4):
                ep = {
                    "titulo": f"Episódio {ep_num}: Risadas Gravadas",
                    "numero": ep_num,
                    "temporada": 1,
                    "duracao_minutos": random.randint(20, 30), # Comédias são mais curtas
                    "nota": round(random.uniform(7.0, 9.5), 1),
                    "serie_id": serie_id
                }
                client.post("/episodios/", json=ep)
        else:
            log(f"Falha ao criar série {s['titulo']}: {resp.text}", "ERRO")

    # 5. ASSOCIAÇÕES (Ligando Atores a Filmes e Séries)
    print("\n--- Criando Associações Específicas e Aleatórias ---")
    
    # Associações "Reais"
    for ator_nome, obra_titulo in ASSOCIACOES_ESPECIFICAS:
        ator_id = mapa_atores.get(ator_nome)
        
        # Tenta achar em filmes
        filme_id = mapa_filmes.get(obra_titulo)
        if filme_id and ator_id:
            resp = client.post(f"/filmes/{filme_id}/atores/{ator_id}")
            if resp.status_code == 200:
                log(f"[Real] Filme '{obra_titulo}' <-> Ator '{ator_nome}'", "SUCESSO")
        
        # Tenta achar em séries
        serie_id = mapa_series.get(obra_titulo)
        if serie_id and ator_id:
            resp = client.post(f"/series/{serie_id}/atores/{ator_id}")
            if resp.status_code == 200:
                log(f"[Real] Série '{obra_titulo}' <-> Ator '{ator_nome}'", "SUCESSO")

    # Associações Aleatórias (Para garantir volume)
    lista_atores_ids = list(mapa_atores.values())
    
    for titulo, f_id in mapa_filmes.items():
        if not lista_atores_ids: break
        atores_random = random.sample(lista_atores_ids, k=min(3, len(lista_atores_ids))) # Elencos de comédia costumam ser maiores
        for a_id in atores_random:
            client.post(f"/filmes/{f_id}/atores/{a_id}")
            
    for titulo, s_id in mapa_series.items():
        if not lista_atores_ids: break
        atores_random = random.sample(lista_atores_ids, k=min(3, len(lista_atores_ids)))
        for a_id in atores_random:
            client.post(f"/series/{s_id}/atores/{a_id}")

    print("\n=== RODANDO TESTES AUTOMATIZADOS DE ROTAS ===")

    # Teste GET (Filtro)
    resp = client.get("/filmes/?genero=Comédia")
    log(f"Teste GET Filtro (Comédia): {len(resp.json())} filmes encontrados", "INFO")

    # Teste PATCH (Update)
    if mapa_filmes:
        primeiro_filme_id = list(mapa_filmes.values())[0]
        titulo_antigo = list(mapa_filmes.keys())[0]
        resp = client.patch(f"/filmes/{primeiro_filme_id}", json={"nota": 10.0}) # Filme de comédia perfeito
        if resp.status_code == 200:
            log(f"Teste PATCH: Nota de '{titulo_antigo}' atualizada para 10.0", "SUCESSO")
        else:
            log("Teste PATCH falhou", "ERRO")

    # Teste DELETE
    filme_ruim = {"titulo": "Comédia Sem Graça", "ano": 2025, "genero": "Sátira", "nota": 2.5}
    resp = client.post("/filmes/", json=filme_ruim)
    if resp.status_code == 201:
        id_del = resp.json()["id"]
        log("Filme temporário criado para teste de delete.", "INFO")
        resp_del = client.delete(f"/filmes/{id_del}")
        if resp_del.status_code == 200:
            log(f"Teste DELETE: Filme temporário removido com sucesso.", "SUCESSO")
        else:
            log(f"Teste DELETE falhou: {resp_del.text}", "ERRO")

    # Estatísticas Finais
    resp = client.get("/filmes/stats/geral")
    if resp.status_code == 200:
        log(f"Estatísticas Finais: {resp.json()}", "INFO")

    log("=== PROCESSO FINALIZADO ===")

if __name__ == "__main__":
    run()