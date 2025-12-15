from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional, TYPE_CHECKING
from .filme_ator import FilmeAtor

if TYPE_CHECKING:
    from .diretor import Diretor
    from .ator import Ator

class FilmeBase(SQLModel): # indices para usar na filtragem
    titulo: str = Field(index=True) 
    ano: int = Field(index=True) 
    genero: str = Field(index=True) 
    nota: float = Field(default=0.0)
    diretor_id: int | None = Field(default=None, foreign_key="diretor.id") # chave estrangeira id do diretor

class Filme(FilmeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    # relacionamentos dos filmes com diretor e com atores
    diretor: Optional["Diretor"] = Relationship(back_populates="filmes")
    atores: List["Ator"] = Relationship(back_populates="filmes", link_model=FilmeAtor) #relacionamento N:N, entao usamos a tabela intermediaria para conexão