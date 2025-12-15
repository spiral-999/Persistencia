from fastapi import FastAPI
from rotas import filmes, diretores, atores, series, episodios

app = FastAPI(title="API Catálogo de Cinema e Séries")

app.include_router(filmes.router)
app.include_router(diretores.router)
app.include_router(atores.router)
app.include_router(series.router)
app.include_router(episodios.router)