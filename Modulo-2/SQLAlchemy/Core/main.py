import logging
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, insert, select, text
from datetime import date

# --- CONCEITO: LOGGING (Slide 33) ---
# Fundamental para ver o SQL "traduzido" pelo dialeto no console.
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# --- CONCEITO: ENGINE e DIALETO (Slide 4 e 7) ---
# O Engine gerencia o Pool de conexões e sabe falar o dialeto (SQLite neste caso).
# echo=True faz o mesmo que o logging acima, mas aqui deixamos explícito para didática.
engine = create_engine("sqlite:///meu_banco_core.sqlite", echo=False)

# --- CONCEITO: METADATA e SCHEMA (Slide 8) ---
# O MetaData é o "catálogo" que guarda as definições das tabelas em memória.
metadata = MetaData()

# Definição da Tabela (Core puro)
pessoas = Table("pessoas", metadata,
    Column("id", Integer, primary_key=True),
    Column("nome", String(50), nullable=False),
    Column("dt_nasc", Date, nullable=False),
    Column("fone", String(15)) # Aumentei o tamanho para segurança
)

# Criação física das tabelas (DDL)
metadata.create_all(engine)

# --- CONCEITO: CONTEXTO TRANSACIONAL (Slide 9) ---
# 'engine.begin()' abre uma transação e dá COMMIT automático no final se não houver erro.
# Se houver erro, ele faz ROLLBACK automático.
try:
    with engine.begin() as conn:
        # CONCEITO: INSERT EM LOTE (Slide 8)
        # Mais performático que inserir um por um.
        conn.execute(
            insert(pessoas),
            [
                {"nome": "João Pedro", "dt_nasc": date(1995, 4, 12), "fone": "88999998888"},
                {"nome": "Maria", "dt_nasc": date(1990, 8, 23), "fone": "85912345678"},
                {"nome": "José", "dt_nasc": date(1988, 1, 3), "fone": "85987654321"},
            ],
        )
        print("✅ Dados inseridos com sucesso (Transação Commitada)!")
except Exception as e:
    print(f"❌ Erro na transação: {e}")

# --- CONCEITO: CONSULTAS E FILTROS (Slide 14) ---
# 'engine.connect()' abre uma conexão, mas não inicia transação de escrita obrigatória (autocommit mode em alguns drivers).
with engine.connect() as conn:
    print("\n--- Consulta com SELECT e WHERE (Pythonic) ---")
    # Query: SELECT * FROM pessoas WHERE dt_nasc > '1990-01-01'
    stmt = select(pessoas).where(pessoas.c.dt_nasc > date(1990, 1, 1))
    
    result = conn.execute(stmt)
    for row in result:
        # Acesso aos dados como tupla nomeada ou objeto row
        print(f"Nome: {row.nome}, Nasc: {row.dt_nasc}")

    # --- CONCEITO: SQL PURO / TEXT (Slide 9 e 10) ---
    print("\n--- Consulta Híbrida com Text (SQL Puro) ---")
    # Útil para queries muito complexas ou específicas do banco.
    stmt_sql = text("SELECT nome FROM pessoas WHERE nome LIKE :letra")
    result_sql = conn.execute(stmt_sql, {"letra": "J%"}) # Parâmetro seguro
    for row in result_sql:
        print(f"Começa com J: {row.nome}")

# --- CONCEITO: REFLEXÃO / REFLECTION (Slide 13) ---
print("\n--- Reflexão (Lendo o banco existente) ---")
metadata_reflexao = MetaData()
# Lê o banco e recria o objeto Table 'pessoas' automaticamente na memória
metadata_reflexao.reflect(bind=engine)

for table_name in metadata_reflexao.tables.keys():
    print(f"Tabela encontrada via reflexão: {table_name}")