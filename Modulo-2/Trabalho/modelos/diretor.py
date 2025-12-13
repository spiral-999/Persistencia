from sqlmodel import SQLModel, Field, Relationship
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .filme import Filme

class DiretorBase(SQLModel):
    nome: str = Field(index=True)
    nacionalidade: str

class Diretor(DiretorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    # Relacionamento: Um diretor tem vários filmes
    filmes: List["Filme"] = Relationship(back_populates="diretor")