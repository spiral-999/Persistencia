from beanie import Document
from pydantic import Field

class Diretor(Document):
    nome: str = Field(index=True)
    nacionalidade: str

    class Settings:
        name = "diretores"