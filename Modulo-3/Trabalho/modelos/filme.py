from beanie import Document, Link
from pydantic import Field
from typing import Optional
from modelos.diretor import Diretor
from modelos.ator import Ator

class Filme(Document):
    titulo: str = Field(index=True)
    ano: int = Field(index=True)
    genero: str = Field(index=True)
    nota: float = 0.0
    diretor: Optional[Link[Diretor]] = None
    atores: list[Link[Ator]] = []

    class Settings:
        name = "filmes"