from beanie import Document, Link
from pydantic import Field
from modelos.serie import Serie

class Episodio(Document):
    titulo: str
    numero: int
    temporada: int
    duracao_minutos: int
    nota: float = 0.0
    serie: Link[Serie]

    class Settings:
        name = "episodios"