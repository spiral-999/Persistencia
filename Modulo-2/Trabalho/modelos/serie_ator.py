from sqlmodel import SQLModel, Field

# tabela intermediaria para garantir a conexão N:N de series e atores
class SerieAtor(SQLModel, table=True):
    serie_id: int | None = Field(default=None, foreign_key="serie.id", primary_key=True)
    ator_id: int | None = Field(default=None, foreign_key="ator.id", primary_key=True)