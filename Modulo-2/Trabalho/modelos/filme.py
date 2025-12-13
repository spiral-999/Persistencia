from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional, TYPE_CHECKING
from .filme_ator import FilmeAtor

if TYPE_CHECKING:
    from .diretor import Diretor
    from .ator import Ator

class FilmeBase(SQLModel):
    titulo: str = Field(index=True)
    ano: int
    genero: str
    nota: float = Field(default=0.0) # IMDB nota
    diretor_id: int | None = Field(default=None, foreign_key="diretor.id")

class Filme(FilmeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    # Relacionamento: Um filme tem um diretor
    diretor: Optional["Diretor"] = Relationship(back_populates="filmes")
    
    # Relacionamento N:N com atores
    atores: List["Ator"] = Relationship(back_populates="filmes", link_model=FilmeAtor)