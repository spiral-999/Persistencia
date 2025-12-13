from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select, func
from typing import List, Optional
from database import get_session
from modelos import Filme, Diretor, Ator, FilmeAtor # Importando do models/__init__.py

router = APIRouter(prefix="/filmes", tags=["Filmes"])

# --- CRUD BÁSICO ---

@router.post("/", response_model=Filme)
def criar_filme(filme: Filme, session: Session = Depends(get_session)):
    session.add(filme)
    session.commit()
    session.refresh(filme)
    return filme

@router.get("/{filme_id}", response_model=Filme)
def obter_filme(filme_id: int, session: Session = Depends(get_session)):
    filme = session.get(Filme, filme_id)
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme

@router.patch("/{filme_id}", response_model=Filme)
def atualizar_filme(filme_id: int, dados_novos: Filme, session: Session = Depends(get_session)):
    filme_db = session.get(Filme, filme_id)
    if not filme_db:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    
    dados = dados_novos.model_dump(exclude_unset=True)
    for key, value in dados.items():
        setattr(filme_db, key, value)
        
    session.add(filme_db)
    session.commit()
    session.refresh(filme_db)
    return filme_db

@router.delete("/{filme_id}")
def deletar_filme(filme_id: int, session: Session = Depends(get_session)):
    filme = session.get(Filme, filme_id)
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    session.delete(filme)
    session.commit()
    return {"message": "Filme deletado com sucesso"}

# --- CONSULTAS REQUERIDAS & FILTROS ---

# Requisito: Listagens filtradas, Busca por texto, Filtro por ano, Classificação
@router.get("/", response_model=List[Filme])
def listar_filmes(
    session: Session = Depends(get_session),
    titulo: Optional[str] = Query(None, description="Busca por parte do título"),
    ano: Optional[int] = Query(None, description="Filtro exato de ano"),
    genero: Optional[str] = Query(None, description="Filtro exato de gênero"),
    ordenar_por_ano: bool = Query(False, description="Se verdadeiro, ordena do mais recente para o antigo"),
    offset: int = 0,
    limit: int = 10
):
    query = select(Filme)

    if titulo:
        query = query.where(Filme.titulo.contains(titulo))
    if ano:
        query = query.where(Filme.ano == ano)
    if genero:
        query = query.where(Filme.genero == genero)
    
    if ordenar_por_ano:
        query = query.order_by(Filme.ano.desc())
    
    query = query.offset(offset).limit(limit)
    return session.exec(query).all()

# Requisito: Agregações e contagens
@router.get("/geral/contagem")
def contar_filmes(session: Session = Depends(get_session)):
    """Retorna o número total de filmes cadastrados."""
    count = session.exec(select(func.count()).select_from(Filme)).one()
    return {"total_filmes": count}

# --- RELACIONAMENTO N:N (Filme <-> Ator) ---

@router.post("/{filme_id}/atores/{ator_id}")
def adicionar_ator_ao_filme(filme_id: int, ator_id: int, session: Session = Depends(get_session)):
    """Cria a relação entre um Filme e um Ator."""
    filme = session.get(Filme, filme_id)
    ator = session.get(Ator, ator_id)
    
    if not filme or not ator:
        raise HTTPException(status_code=404, detail="Filme ou Ator não encontrado")
    
    # Cria a ligação na tabela associativa
    link = FilmeAtor(filme_id=filme_id, ator_id=ator_id)
    session.add(link)
    try:
        session.commit()
    except Exception:
        session.rollback()
        raise HTTPException(status_code=400, detail="Este ator já está associado a este filme")
        
    return {"message": f"Ator {ator.nome} adicionado ao filme {filme.titulo}"}

@router.get("/{filme_id}/atores", response_model=List[Ator])
def listar_atores_do_filme(filme_id: int, session: Session = Depends(get_session)):
    """Lista todos os atores de um filme específico."""
    filme = session.get(Filme, filme_id)
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme.atores