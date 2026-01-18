from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .serie import Serie

class EpisodioBase(SQLModel):
    titulo: str
    numero: int
    temporada: int
    duracao_minutos: int
    nota: float = Field(default=0.0)

class Episodio(EpisodioBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    serie_id: int = Field(foreign_key="serie.id") # obrigatorio um episodio ter uma serie
    
    # relacionamentos do episodio
    serie: Optional["Serie"] = Relationship(back_populates="episodios")

class EpisodioRead(EpisodioBase):
    id: int