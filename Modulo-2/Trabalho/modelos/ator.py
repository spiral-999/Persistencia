from sqlmodel import SQLModel, Field, Relationship
from typing import List, TYPE_CHECKING
from datetime import date, datetime
from pydantic import field_validator

# Importação necessária para o link_model funcionar
from .filme_ator import FilmeAtor

if TYPE_CHECKING:
    from .filme import Filme

class AtorBase(SQLModel):
    nome: str = Field(index=True)
    data_nascimento: date

    # Validador para garantir que strings sejam convertidas para date
    @field_validator("data_nascimento", mode="before")
    @classmethod
    def parse_data_nascimento(cls, v):
        if isinstance(v, str):
            # Tenta converter string "YYYY-MM-DD" para objeto date
            return datetime.strptime(v, "%Y-%m-%d").date()
        return v

class Ator(AtorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    # Relacionamento N:N com filmes
    # IMPORTANTE: link_model usa a classe FilmeAtor, não uma string
    filmes: List["Filme"] = Relationship(back_populates="atores", link_model=FilmeAtor)