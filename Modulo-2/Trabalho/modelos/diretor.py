from sqlmodel import SQLModel, Field, Relationship
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .filme import Filme
    from .serie import Serie

class DiretorBase(SQLModel):
    nome: str = Field(index=True)
    nacionalidade: str

class Diretor(DiretorBase, table=True):
    id: int | None = Field(default=None, primary_key=True) # id como chave primaria e opcional 

    # relacionamentos do diretor com filmes e series 
    filmes: List["Filme"] = Relationship(back_populates="diretor")
    series: List["Serie"] = Relationship(back_populates="diretor")