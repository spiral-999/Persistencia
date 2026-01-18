from beanie import Document, Link
from pydantic import Field
from typing import Optional
from modelos.diretor import Diretor
from modelos.ator import Ator

class Serie(Document):
    titulo: str = Field(index=True)
    ano_inicio: int = Field(index=True)
    genero: str
    descricao: str | None = None
    
    diretor: Optional[Link[Diretor]] = None
    atores: list[Link[Ator]] = []

    class Settings:
        name = "series"