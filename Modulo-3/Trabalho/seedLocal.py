import asyncio
from datetime import date
from database import init_db
from modelos.ator import Ator
from modelos.diretor import Diretor
from modelos.filme import Filme
from modelos.serie import Serie
from modelos.episodio import Episodio

DADOS_DIRETORES = [
    {"nome": "Todd Phillips", "nacionalidade": "Americano"},
    {"nome": "Judd Apatow", "nacionalidade": "Americano"},
    {"nome": "Adam McKay", "nacionalidade": "Americano"},
    {"nome": "Paul Feig", "nacionalidade": "Americano"},
    {"nome": "Edgar Wright", "nacionalidade": "Britânico"},
    {"nome": "Ivan Reitman", "nacionalidade": "Canadense"},
    {"nome": "Mel Brooks", "nacionalidade": "Americano"},
    {"nome": "Wes Anderson", "nacionalidade": "Americano"},
    {"nome": "Rob Reiner", "nacionalidade": "Americano"},
    {"nome": "Taika Waititi", "nacionalidade": "Neozelandês"}
]

DADOS_ATORES = [
    {"nome": "Steve Carell", "data_nascimento": "1962-08-16"},
    {"nome": "Will Ferrell", "data_nascimento": "1967-07-16"},
    {"nome": "Seth Rogen", "data_nascimento": "1982-04-15"},
    {"nome": "Kristen Wiig", "data_nascimento": "1973-08-22"},
    {"nome": "Simon Pegg", "data_nascimento": "1970-02-14"},
    {"nome": "Bill Murray", "data_nascimento": "1950-09-21"},
    {"nome": "Gene Wilder", "data_nascimento": "1933-06-11"},
    {"nome": "Jason Sudeikis", "data_nascimento": "1975-09-18"},
    {"nome": "Andy Samberg", "data_nascimento": "1978-08-18"},
    {"nome": "Tina Fey", "data_nascimento": "1970-05-18"}
]

DADOS_FILMES = [
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

DADOS_SERIES = [
    {"titulo": "The Office", "ano_inicio": 2005, "genero": "Mockumentary", "descricao": "Cotidiano de um escritório de papel."},
    {"titulo": "Ted Lasso", "ano_inicio": 2020, "genero": "Esporte/Comédia", "descricao": "Treinador americano na Inglaterra."},
    {"titulo": "Brooklyn Nine-Nine", "ano_inicio": 2013, "genero": "Policial/Comédia", "descricao": "Delegacia de polícia no Brooklyn."},
    {"titulo": "Freaks and Geeks", "ano_inicio": 1999, "genero": "Teen/Comédia", "descricao": "Vida no ensino médio nos anos 80."},
    {"titulo": "Parks and Recreation", "ano_inicio": 2009, "genero": "Mockumentary", "descricao": "Departamento de parques em Indiana."},
    {"titulo": "30 Rock", "ano_inicio": 2006, "genero": "Sátira", "descricao": "Bastidores de um programa de TV."},
    {"titulo": "Community", "ano_inicio": 2009, "genero": "Sitcom", "descricao": "Grupo de estudos em faculdade comunitária."},
    {"titulo": "Seinfeld", "ano_inicio": 1989, "genero": "Sitcom", "descricao": "Show sobre nada."},
    {"titulo": "Arrested Development", "ano_inicio": 2003, "genero": "Sitcom", "descricao": "Família rica que perdeu tudo."},
    {"titulo": "What We Do in the Shadows", "ano_inicio": 2019, "genero": "Terror/Comédia", "descricao": "Vampiros dividindo casa em Staten Island."}
]

ASSOCIACOES = [
    ("Steve Carell", "The Office"),
    ("Steve Carell", "O Âncora: A Lenda de Ron Burgundy"),
    ("Will Ferrell", "Quase Irmãos"),
    ("Will Ferrell", "The Office"),
    ("Seth Rogen", "Ligeiramente Grávidos"),
    ("Seth Rogen", "Freaks and Geeks"),
    ("Kristen Wiig", "Missão Madrinha de Casamento"),
    ("Simon Pegg", "Chumbo Grosso"),
    ("Bill Murray", "Os Caça-Fantasmas"),
    ("Bill Murray", "O Grande Hotel Budapeste"),
    ("Gene Wilder", "Banzé no Oeste"),
    ("Jason Sudeikis", "Ted Lasso"),
    ("Andy Samberg", "Brooklyn Nine-Nine"),
    ("Tina Fey", "30 Rock"),
    ("Paul Rudd", "O Âncora")
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
                duracao_minutos=22,
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

    print("database de Comédia atualizada (local)")


if __name__ == "__main__":
    asyncio.run(povoar_banco())