import os
from datetime import date
from typing import Optional
from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# --- CONCEITO: CONFIGURAÇÃO VIA .ENV (Slide 35-37) ---
# Simulação de carregamento do .env
os.environ["DATABASE_URL"] = "sqlite:///exemplo-orm-completo.db"
db_url = os.getenv("DATABASE_URL")

# Configuração do Engine
engine = create_engine(db_url, echo=False)

# --- CONCEITO: MODELAGEM DECLARATIVA MODERNA (Slide 27) ---
# Uso de 'Mapped' e type hints (int, str) substitui a sintaxe antiga Column(Integer...)
class Base(DeclarativeBase):
    pass

class Aluno(Base):
    __tablename__ = 'alunos'
    
    # Primary Key inferida e obrigatória
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # String(50) define o tamanho no banco. Mapped[str] define o tipo no Python.
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    
    # Optional[str] mapeia para NULL no banco (nullable=True implícito se não definido o contrário)
    apelido: Mapped[Optional[str]] = mapped_column(String(30))

    # --- CONCEITO: REPR (Slide 27) ---
    # Melhora a visualização no print() e logs
    def __repr__(self) -> str:
        return f"Aluno(id={self.id}, nome='{self.nome}', apelido='{self.apelido}')"

# Criação das tabelas
Base.metadata.create_all(engine)

# --- CONCEITO: SESSION (Slide 31) ---
# A Session gerencia a "Unidade de Trabalho" (Unit of Work).
# Ela guarda os objetos em memória e sincroniza com o banco no commit.
with Session(engine) as session:
    try:
        # 1. CREATE (Adicionando Objetos)
        aluno1 = Aluno(nome="Maria", apelido="Mari")
        aluno2 = Aluno(nome="João") # apelido é None/Null
        
        # 'add' coloca o objeto na sessão, mas ainda não enviou INSERT para o banco
        session.add(aluno1)
        session.add(aluno2)
        
        # 'commit' efetiva a transação no banco (INSERT)
        session.commit()
        print("✅ Alunos persistidos com sucesso!")
        
        # 2. READ (Consultas com sintaxe 2.0)
        print("\n--- Consultando Objetos ---")
        # select(Aluno) substitui session.query(Aluno) nas versões novas
        stmt = select(Aluno).where(Aluno.nome == "Maria")
        
        # 'scalar' pega o primeiro resultado (objeto)
        # 'scalars' pega uma lista de resultados (objetos)
        resultado = session.execute(stmt).scalars().first()
        
        if resultado:
            print(f"Encontrado: {resultado}")
            
            # 3. UPDATE (Alteração de Estado)
            # Ao mudar o atributo, a Session marca o objeto como 'dirty' (sujo)
            resultado.apelido = "Duda"
            session.commit() # O SQLAlchemy detecta a mudança e faz o UPDATE automaticamente
            print(f"Atualizado para: {resultado}")
            
    except Exception as e:
        session.rollback()
        print(f"❌ Erro: {e}")

# --- CONCEITO: CONSULTA GERAL ---
with Session(engine) as session:
    print("\n--- Lista Geral ---")
    alunos = session.execute(select(Aluno)).scalars().all()
    for a in alunos:
        print(a)