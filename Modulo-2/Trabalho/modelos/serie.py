from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional, TYPE_CHECKING
from .serie_ator import SerieAtor
from .diretor import DiretorRead
from .ator import AtorRead
from .episodio import EpisodioRead

if TYPE_CHECKING:
    from .episodio import Episodio
    from .diretor import Diretor
    from .ator import Ator

class SerieBase(SQLModel):
    titulo: str = Field(index=True)
    ano_inicio: int = Field(index=True)
    genero: str = Field(index=True)
    descricao: str | None = None
    diretor_id: int | None = Field(default=None, foreign_key="diretor.id")

class Serie(SerieBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    # relacionamentos das series
    episodios: List["Episodio"] = Relationship(back_populates="serie") # 1:N; 1 series tem n episodios
    diretor: Optional["Diretor"] = Relationship(back_populates="series") # N:1; N diretores tem 1 diretor
    atores: List["Ator"] = Relationship(back_populates="series", link_model=SerieAtor) # N:N; N séries tem N atores

class SerieRead(SerieBase): # modelo de leitura para as consultas aninhadas
    id: int
    diretor: Optional[DiretorRead] = None
    atores: List[AtorRead] = []
    episodios: List[EpisodioRead] = []