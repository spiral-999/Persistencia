import httpx
import random
from datetime import date

# Configuração
BASE_URL = "http://127.0.0.1:8000"

# --- DADOS TEMÁTICOS: TERROR/HORROR ---

DIRETORES = [
    {"nome": "Sam Raimi", "nacionalidade": "Americano"},       # Evil Dead
    {"nome": "Patrick Brice", "nacionalidade": "Americano"},   # Creep
    {"nome": "Wes Craven", "nacionalidade": "Americano"},      # Pânico
    {"nome": "Keenen Ivory Wayans", "nacionalidade": "Americano"}, # Todo Mundo em Pânico
    {"nome": "Andy Muschietti", "nacionalidade": "Argentino"}, # It
    {"nome": "Mike Flanagan", "nacionalidade": "Americano"},   # Hill House
    {"nome": "James Wan", "nacionalidade": "Australiano"},     # Invocação do Mal
    {"nome": "Jordan Peele", "nacionalidade": "Americano"},    # Corra!
    {"nome": "Ari Aster", "nacionalidade": "Americano"},       # Hereditário
    {"nome": "Ti West", "nacionalidade": "Americano"}          # X / Pearl
]

ATORES = [
    {"nome": "Mark Duplass", "data_nascimento": "1976-12-07"},      # Creep
    {"nome": "Matthew Lillard", "data_nascimento": "1970-01-24"},    # Pânico / Scooby Doo
    {"nome": "Bruce Campbell", "data_nascimento": "1958-06-22"},     # Evil Dead
    {"nome": "Neve Campbell", "data_nascimento": "1973-10-03"},      # Pânico
    {"nome": "Anna Faris", "data_nascimento": "1976-11-29"},         # Todo Mundo em Pânico
    {"nome": "Bill Skarsgård", "data_nascimento": "1990-08-09"},     # It (Pennywise)
    {"nome": "Mia Goth", "data_nascimento": "1993-11-30"},           # Pearl
    {"nome": "Patrick Wilson", "data_nascimento": "1973-07-03"},     # Invocação do Mal
    {"nome": "Sarah Paulson", "data_nascimento": "1974-12-17"},      # AHS
    {"nome": "Jenna Ortega", "data_nascimento": "2002-09-27"}        # Pânico (Novo) / Wandinha
]

FILMES = [
    {"titulo": "Evil Dead 2", "ano": 1987, "genero": "Terror/Comédia", "nota": 7.7, "diretor_nome": "Sam Raimi"},
    {"titulo": "Creep", "ano": 2014, "genero": "Found Footage", "nota": 6.3, "diretor_nome": "Patrick Brice"},
    {"titulo": "Pânico", "ano": 1996, "genero": "Slasher", "nota": 7.4, "diretor_nome": "Wes Craven"},
    {"titulo": "Todo Mundo em Pânico", "ano": 2000, "genero": "Paródia", "nota": 6.3, "diretor_nome": "Keenen Ivory Wayans"},
    {"titulo": "It: A Coisa", "ano": 2017, "genero": "Sobrenatural", "nota": 7.3, "diretor_nome": "Andy Muschietti"},
    {"titulo": "Hereditário", "ano": 2018, "genero": "Terror Psicológico", "nota": 7.3, "diretor_nome": "Ari Aster"},
    {"titulo": "X: A Marca da Morte", "ano": 2022, "genero": "Slasher", "nota": 6.6, "diretor_nome": "Ti West"},
    {"titulo": "Invocação do Mal", "ano": 2013, "genero": "Sobrenatural", "nota": 7.5, "diretor_nome": "James Wan"},
    {"titulo": "Corra!", "ano": 2017, "genero": "Suspense", "nota": 7.8, "diretor_nome": "Jordan Peele"},
    {"titulo": "Pearl", "ano": 2022, "genero": "Slasher", "nota": 7.0, "diretor_nome": "Ti West"}
]

SERIES = [
    {"titulo": "The Creep Tapes", "ano_inicio": 2024, "genero": "Found Footage", "descricao": "Spin-off da franquia Creep.", "diretor_nome": "Patrick Brice"},
    {"titulo": "It: Welcome to Derry", "ano_inicio": 2025, "genero": "Terror", "descricao": "Prequel de It.", "diretor_nome": "Andy Muschietti"},
    {"titulo": "Ash vs Evil Dead", "ano_inicio": 2015, "genero": "Terror/Comédia", "descricao": "Ash Williams volta a caçar demônios.", "diretor_nome": "Sam Raimi"},
    {"titulo": "A Maldição da Residência Hill", "ano_inicio": 2018, "genero": "Drama/Terror", "descricao": "Família assombrada pelo passado.", "diretor_nome": "Mike Flanagan"},
    {"titulo": "American Horror Story", "ano_inicio": 2011, "genero": "Antologia", "descricao": "Histórias de horror variadas."},
    {"titulo": "Chucky", "ano_inicio": 2021, "genero": "Slasher", "descricao": "O boneco assassino retorna."},
    {"titulo": "Hannibal", "ano_inicio": 2013, "genero": "Crime/Terror", "descricao": "Dr. Hannibal Lecter antes da prisão."},
    {"titulo": "Bates Motel", "ano_inicio": 2013, "genero": "Suspense", "descricao": "Origem de Norman Bates."},
    {"titulo": "Missa da Meia-Noite", "ano_inicio": 2021, "genero": "Terror Religioso", "descricao": "Ilha isolada e milagres sombrios.", "diretor_nome": "Mike Flanagan"},
    {"titulo": "Stranger Things", "ano_inicio": 2016, "genero": "Sci-Fi/Terror", "descricao": "Mundo invertido e Demogorgons."}
]

# Associações específicas (Nome Ator -> Título da Obra) para garantir realismo
ASSOCIACOES_ESPECIFICAS = [
    ("Mark Duplass", "Creep"),
    ("Mark Duplass", "The Creep Tapes"),
    ("Matthew Lillard", "Pânico"),
    ("Matthew Lillard", "Todo Mundo em Pânico"), # Curiosidade: ele não fez o paródia, mas vamos forçar pra testar N:N :D
    ("Bruce Campbell", "Evil Dead 2"),
    ("Bruce Campbell", "Ash vs Evil Dead"),
    ("Neve Campbell", "Pânico"),
    ("Anna Faris", "Todo Mundo em Pânico"),
    ("Bill Skarsgård", "It: A Coisa"),
    ("Bill Skarsgård", "It: Welcome to Derry"),
    ("Mia Goth", "Pearl"),
    ("Mia Goth", "X: A Marca da Morte"),
    ("Patrick Wilson", "Invocação do Mal"),
    ("Jenna Ortega", "Pânico"),
    ("Sarah Paulson", "American Horror Story")
]

def log(msg, tipo="INFO"):
    cores = {"INFO": "\033[94m", "SUCESSO": "\033[92m", "ERRO": "\033[91m", "RESET": "\033[0m"}
    print(f"{cores.get(tipo, '')}[{tipo}] {msg}{cores['RESET']}")

def run():
    client = httpx.Client(base_url=BASE_URL, timeout=15.0)
    
    # Mapas para guardar IDs gerados { "Nome": ID }
    mapa_diretores = {}
    mapa_atores = {}
    mapa_filmes = {} # { "Titulo": ID }
    mapa_series = {} # { "Titulo": ID }

    log("=== INICIANDO POVOAMENTO DO BANCO DE DADOS (TEMA: TERROR) ===")

    # 1. CRIAR DIRETORES
    print("\n--- Criando Diretores ---")
    for d in DIRETORES:
        resp = client.post("/diretores/", json=d)
        if resp.status_code == 201:
            data = resp.json()
            mapa_diretores[data["nome"]] = data["id"]
            log(f"Diretor criado: {data['nome']} (ID: {data['id']})", "SUCESSO")
        else:
            # Se já existir ou der erro, tentamos buscar pelo nome (num cenário real)
            # Aqui apenas logamos erro
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
        # Tenta achar o ID do diretor pelo nome, senão pega um aleatório
        nome_dir = f.pop("diretor_nome", None)
        diretor_id = mapa_diretores.get(nome_dir)
        
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
                    "titulo": f"Episódio {ep_num}" if ep_num == 1 else f"Episódio {ep_num}",
                    "numero": ep_num,
                    "temporada": 1,
                    "duracao_minutos": random.randint(40, 60),
                    "nota": round(random.uniform(7.0, 9.5), 1),
                    "serie_id": serie_id
                }
                client.post("/episodios/", json=ep)
        else:
            log(f"Falha ao criar série {s['titulo']}: {resp.text}", "ERRO")

    # 5. ASSOCIAÇÕES (Ligando Atores a Filmes e Séries)
    print("\n--- Criando Associações Específicas e Aleatórias ---")
    
    # Associações "Reais" (Definidas na lista ASSOCIACOES_ESPECIFICAS)
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

    # Associações Aleatórias (Para garantir volume, todo filme ter elenco)
    # Garante que todo filme tenha pelo menos +2 atores aleatórios
    lista_atores_ids = list(mapa_atores.values())
    
    for titulo, f_id in mapa_filmes.items():
        if not lista_atores_ids: break
        atores_random = random.sample(lista_atores_ids, k=min(2, len(lista_atores_ids)))
        for a_id in atores_random:
            client.post(f"/filmes/{f_id}/atores/{a_id}") # Pode dar erro se já existir, ignoramos
            
    for titulo, s_id in mapa_series.items():
        if not lista_atores_ids: break
        atores_random = random.sample(lista_atores_ids, k=min(2, len(lista_atores_ids)))
        for a_id in atores_random:
            client.post(f"/series/{s_id}/atores/{a_id}")

    print("\n=== RODANDO TESTES AUTOMATIZADOS DE ROTAS ===")

    # Teste GET (Filtro)
    resp = client.get("/filmes/?genero=Slasher")
    log(f"Teste GET Filtro (Slasher): {len(resp.json())} filmes encontrados", "INFO")

    # Teste PATCH (Update)
    if mapa_filmes:
        primeiro_filme_id = list(mapa_filmes.values())[0]
        titulo_antigo = list(mapa_filmes.keys())[0]
        resp = client.patch(f"/filmes/{primeiro_filme_id}", json={"nota": 9.9})
        if resp.status_code == 200:
            log(f"Teste PATCH: Nota de '{titulo_antigo}' atualizada para 9.9", "SUCESSO")
        else:
            log("Teste PATCH falhou", "ERRO")

    # Teste DELETE
    # Vamos criar um "Filme Ruim" só para deletar
    filme_ruim = {"titulo": "Filme Ruim de Terror", "ano": 2025, "genero": "Trash", "nota": 1.0}
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