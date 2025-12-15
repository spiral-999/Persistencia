from sqlmodel import SQLModel, Field, Relationship
from typing import List, TYPE_CHECKING
from datetime import date, datetime
from pydantic import field_validator # para verificar a data(pq coloquei campo de data meudeus)
from .filme_ator import FilmeAtor
from .serie_ator import SerieAtor

if TYPE_CHECKING:
    from .filme import Filme
    from .serie import Serie

class AtorBase(SQLModel):
    nome: str = Field(index=True)
    data_nascimento: date
    @field_validator("data_nascimento", mode="before") # funcãozinha para validar e transformar em objeto date do python
    @classmethod
    def parse_data_nascimento(cls, v):
        if isinstance(v, str):
            return datetime.strptime(v, "%Y-%m-%d").date()
        return v

class Ator(AtorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    # relacionamentos do ator, dois relacionamentos N:N que usam tabelas de ligação
    filmes: List["Filme"] = Relationship(back_populates="atores", link_model=FilmeAtor)
    series: List["Serie"] = Relationship(back_populates="atores", link_model=SerieAtor)