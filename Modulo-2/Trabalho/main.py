from fastapi import FastAPI
from rotas import filmes, diretores, atores
# Importe as rotas que você criou

app = FastAPI(title="API Catálogo de Cinema")

app.include_router(filmes.router)
app.include_router(diretores.router)
app.include_router(atores.router)