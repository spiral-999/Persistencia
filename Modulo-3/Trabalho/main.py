from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import init_db
from rotas import filmes, diretores, atores, series, episodios

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(
    title="API Catálogo de Cinema com MongoDB",
    description="Trabalho 3 - FastAPI e Beanie",
    lifespan=lifespan
)

app.include_router(filmes.router)
app.include_router(diretores.router)
app.include_router(atores.router)
app.include_router(series.router)
app.include_router(episodios.router)

@app.get("/")
def root():
    return {"mensagem": "MongoDB conectado e rodando"}