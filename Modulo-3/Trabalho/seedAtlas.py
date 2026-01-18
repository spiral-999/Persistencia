import asyncio
from datetime import date
from database import init_db
from modelos.ator import Ator
from modelos.diretor import Diretor
from modelos.filme import Filme
from modelos.serie import Serie
from modelos.episodio import Episodio


DADOS_DIRETORES = [
    {"nome": "Sam Raimi", "nacionalidade": "Americano"},
    {"nome": "Patrick Brice", "nacionalidade": "Americano"},
    {"nome": "Wes Craven", "nacionalidade": "Americano"},
    {"nome": "Keenen Ivory Wayans", "nacionalidade": "Americano"},
    {"nome": "Andy Muschietti", "nacionalidade": "Argentino"},
    {"nome": "Mike Flanagan", "nacionalidade": "Americano"},
    {"nome": "James Wan", "nacionalidade": "Australiano"},
    {"nome": "Jordan Peele", "nacionalidade": "Americano"},
    {"nome": "Ari Aster", "nacionalidade": "Americano"},
    {"nome": "Ti West", "nacionalidade": "Americano"}
]

DADOS_ATORES = [
    {"nome": "Mark Duplass", "data_nascimento": "1976-12-07"},
    {"nome": "Matthew Lillard", "data_nascimento": "1970-01-24"},
    {"nome": "Bruce Campbell", "data_nascimento": "1958-06-22"},
    {"nome": "Neve Campbell", "data_nascimento": "1973-10-03"},
    {"nome": "Anna Faris", "data_nascimento": "1976-11-29"},
    {"nome": "Bill Skarsgård", "data_nascimento": "1990-08-09"}, 
    {"nome": "Mia Goth", "data_nascimento": "1993-11-30"},
    {"nome": "Patrick Wilson", "data_nascimento": "1973-07-03"},
    {"nome": "Sarah Paulson", "data_nascimento": "1974-12-17"},
    {"nome": "Jenna Ortega", "data_nascimento": "2002-09-27"}
]

DADOS_FILMES = [
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

DADOS_SERIES = [
    {"titulo": "The Creep Tapes", "ano_inicio": 2024, "genero": "Found Footage", "descricao": "Spin-off da franquia Creep."},
    {"titulo": "It: Welcome to Derry", "ano_inicio": 2025, "genero": "Terror", "descricao": "Prequel de It."},
    {"titulo": "Ash vs Evil Dead", "ano_inicio": 2015, "genero": "Terror/Comédia", "descricao": "Ash Williams volta a caçar demônios."},
    {"titulo": "A Maldição da Residência Hill", "ano_inicio": 2018, "genero": "Drama/Terror", "descricao": "Família assombrada pelo passado."},
    {"titulo": "American Horror Story", "ano_inicio": 2011, "genero": "Antologia", "descricao": "Histórias de horror variadas."},
    {"titulo": "Chucky", "ano_inicio": 2021, "genero": "Slasher", "descricao": "O boneco assassino retorna."},
    {"titulo": "Hannibal", "ano_inicio": 2013, "genero": "Crime/Terror", "descricao": "Dr. Hannibal Lecter antes da prisão."},
    {"titulo": "Bates Motel", "ano_inicio": 2013, "genero": "Suspense", "descricao": "Origem de Norman Bates."},
    {"titulo": "Missa da Meia-Noite", "ano_inicio": 2021, "genero": "Terror Religioso", "descricao": "Ilha isolada e milagres sombrios."},
    {"titulo": "Stranger Things", "ano_inicio": 2016, "genero": "Sci-Fi/Terror", "descricao": "Mundo invertido e Demogorgons."}
]

ASSOCIACOES = [
    ("Mark Duplass", "Creep"),
    ("Matthew Lillard", "Pânico"),
    ("Matthew Lillard", "Todo Mundo em Pânico"),
    ("Bruce Campbell", "Evil Dead 2"),
    ("Neve Campbell", "Pânico"),
    ("Anna Faris", "Todo Mundo em Pânico"),
    ("Bill Skarsgård", "It: A Coisa"),
    ("Mia Goth", "Pearl"),
    ("Mia Goth", "X: A Marca da Morte"),
    ("Patrick Wilson", "Invocação do Mal"),
    ("Jenna Ortega", "Pânico"),
    ("Sarah Paulson", "American Horror Story")
]

async def povoar_banco():
    print("Conectando no MongoDB")
    await init_db()

    print("Limpando coleções velhas, para garantir")
    await Filme.delete_all()
    await Ator.delete_all()
    await Diretor.delete_all()
    await Serie.delete_all()
    await Episodio.delete_all()

    mapa_diretores = {}
    mapa_atores = {}
    mapa_filmes = {}
    mapa_series = {}

    print("Adicionando os Diretores")
    for dados in DADOS_DIRETORES:
        diretor = Diretor(**dados)
        await diretor.insert()
        mapa_diretores[dados["nome"]] = diretor
    
    print("Adicionando os Atores")
    for dados in DADOS_ATORES:
        dados_copy = dados.copy()
        dados_copy["data_nascimento"] = date.fromisoformat(dados["data_nascimento"])
        ator = Ator(**dados_copy)
        await ator.insert()
        mapa_atores[dados["nome"]] = ator

    print("Adicionando os Filmes")
    for dados in DADOS_FILMES:
        dados_copy = dados.copy()
        nome_diretor = dados_copy.pop("diretor_nome", None)
        diretor_obj = mapa_diretores.get(nome_diretor)
        filme = Filme(**dados_copy, diretor=diretor_obj, atores=[])
        await filme.insert()
        mapa_filmes[dados["titulo"]] = filme

    print("Adicionando Séries e Episódios")
    for dados in DADOS_SERIES:
        dados_copy = dados.copy()
        dados_copy.pop("diretor_nome", None) 
        
        serie = Serie(**dados_copy)
        await serie.insert()
        mapa_series[dados["titulo"]] = serie
        for i in range(1, 4):
            ep = Episodio(
                titulo=f"Capítulo {i}",
                numero=i,
                temporada=1,
                duracao_minutos=45,
                nota=8.5,
                serie=serie
            )
            await ep.insert()

    print("Fazendo as Associações")
    for nome_ator, titulo_obra in ASSOCIACOES:
        ator = mapa_atores.get(nome_ator)
        if titulo_obra in mapa_filmes:
            filme = mapa_filmes[titulo_obra]
            if ator:
                filme.atores.append(ator)
                await filme.save()

    print("database de Terror atualizada (atlas)")

if __name__ == "__main__":
    asyncio.run(povoar_banco())