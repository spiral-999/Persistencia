from beanie import Document
from pydantic import Field
from datetime import date, datetime
from pydantic import field_validator

class Ator(Document):
    nome: str = Field(index=True)
    data_nascimento: date
    @field_validator("data_nascimento", mode="before")
    @classmethod
    def parse_data_nascimento(cls, v):
        if isinstance(v, str):
            return datetime.strptime(v, "%Y-%m-%d").date()
        return v

    class Settings:
        name = "atores"