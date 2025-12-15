from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select, func
from typing import List, Optional
from database import get_session
from modelos.filme import Filme
from modelos.ator import Ator
from modelos.filme_ator import FilmeAtor

router = APIRouter(prefix="/filmes", tags=["Filmes"])

# CRUD
@router.post("/", response_model=Filme, status_code=201)
def criar_filme(filme: Filme, session: Session = Depends(get_session)):
    session.add(filme)
    try:
        session.commit()
        session.refresh(filme)
        return filme
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao salvar filme: {e}")

@router.get("/", response_model=List[Filme])
def listar_filmes(
    session: Session = Depends(get_session),
    titulo: Optional[str] = Query(None, description="Busca por parte do título"),
    genero: Optional[str] = Query(None, description="Filtro exato de gênero"),
    ano: Optional[int] = Query(None, description="Filtro por ano"),
    nota_minima: Optional[float] = Query(None, description="Nota mínima IMDB"),
    offset: int = 0,
    limit: int = 10
):
    query = select(Filme)
    if titulo:
        query = query.where(Filme.titulo.contains(titulo))
    if genero:
        query = query.where(Filme.genero == genero)
    if ano:
        query = query.where(Filme.ano == ano)
    if nota_minima:
        query = query.where(Filme.nota >= nota_minima)
        
    return session.exec(query.offset(offset).limit(limit)).all()

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

# Relacionamento N:N
@router.post("/{filme_id}/atores/{ator_id}")
def adicionar_ator_ao_filme(filme_id: int, ator_id: int, session: Session = Depends(get_session)):
    filme = session.get(Filme, filme_id)
    ator = session.get(Ator, ator_id)
    if not filme or not ator:
        raise HTTPException(status_code=404, detail="Filme ou Ator não encontrado")
    
    link_existente = session.exec(
        select(FilmeAtor).where(FilmeAtor.filme_id == filme_id, FilmeAtor.ator_id == ator_id)
    ).first()
    
    if link_existente:
        raise HTTPException(status_code=400, detail="Ator já está neste filme")

    link = FilmeAtor(filme_id=filme_id, ator_id=ator_id)
    session.add(link)
    session.commit()
    return {"message": f"Ator {ator.nome} adicionado ao filme {filme.titulo}"}

# Estatísticas
@router.get("/stats/geral")
def estatisticas_filmes(session: Session = Depends(get_session)):
    total_filmes = session.exec(select(func.count(Filme.id))).one()
    media_notas = session.exec(select(func.avg(Filme.nota))).one()
    return {
        "total_filmes": total_filmes,
        "media_notas_imdb": round(media_notas, 2) if media_notas else 0
    }