from sqlmodel import SQLModel, Field

# tabela intermediaria para garantir a conexão N:N de filmes e atores
class FilmeAtor(SQLModel, table=True):
    filme_id: int | None = Field(default=None, foreign_key="filme.id", primary_key=True)
    ator_id: int | None = Field(default=None, foreign_key="ator.id", primary_key=True)