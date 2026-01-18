import os
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from dotenv import load_dotenv
from modelos.ator import Ator
from modelos.diretor import Diretor
from modelos.filme import Filme
from modelos.serie import Serie
from modelos.episodio import Episodio

load_dotenv()
async def init_db():
    db_url = os.getenv("DATABASE_URL", "mongodb://localhost:27017")
    db_name = "catalogo_cinema" 
    client = AsyncIOMotorClient(db_url)
    database = client[db_name]

    await init_beanie(
        database=database,
        document_models=[
            Ator,
            Diretor,
            Filme,
            Serie,
            Episodio
        ]
    )