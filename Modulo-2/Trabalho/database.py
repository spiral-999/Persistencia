import sqlite3
from sqlmodel import create_engine, Session
from sqlalchemy import event, Engine
from dotenv import load_dotenv
import logging
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Configurar o logger (opcional, ajuda a ver o SQL no terminal)
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Configuração do banco de dados
# Garante que se não houver variável, usa um default para não quebrar (opcional)
db_url = os.getenv("DATABASE_URL", "sqlite:///./catalogo_cinema.db")
engine = create_engine(db_url)

def get_session() -> Session:
    with Session(engine) as session:
        yield session

# Configuração específica para SQLite (Foreign Keys)
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):  # somente para o SQLite
       cursor = dbapi_connection.cursor()
       cursor.execute("PRAGMA foreign_keys=ON")
       cursor.close()