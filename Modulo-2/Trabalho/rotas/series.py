from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from typing import List, Optional
from database import get_session
from modelos.serie import Serie
from modelos.episodio import Episodio
from modelos.ator import Ator
from modelos.serie_ator import SerieAtor

router = APIRouter(prefix="/series", tags=["Séries"])

# CREATE
@router.post("/", response_model=Serie, status_code=201)
def criar_serie(serie: Serie, session: Session = Depends(get_session)):
    session.add(serie)
    try:
        session.commit()
        session.refresh(serie)
        return serie
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao criar série: {e}")

# READ com filtros
@router.get("/", response_model=List[Serie])
def listar_series(
    session: Session = Depends(get_session),
    titulo: Optional[str] = Query(None, description="Filtro por título"),
    genero: Optional[str] = Query(None, description="Filtro por gênero"),
    ano_inicio: Optional[int] = Query(None, description="Filtro por ano de início"),
    offset: int = 0,
    limit: int = 10
):
    query = select(Serie)
    
    if titulo:
        query = query.where(Serie.titulo.contains(titulo))
    if genero:
        query = query.where(Serie.genero == genero)
    if ano_inicio:
        query = query.where(Serie.ano_inicio == ano_inicio)
        
    return session.exec(query.offset(offset).limit(limit)).all()

# READ detalhes da série e episódios
@router.get("/{serie_id}", response_model=Serie)
def obter_serie(serie_id: int, session: Session = Depends(get_session)):
    serie = session.get(Serie, serie_id)
    if not serie:
        raise HTTPException(status_code=404, detail="Série não encontrada")
    return serie

@router.get("/{serie_id}/episodios", response_model=List[Episodio])
def listar_episodios_da_serie(serie_id: int, session: Session = Depends(get_session)):
    serie = session.get(Serie, serie_id)
    if not serie:
        raise HTTPException(status_code=404, detail="Série não encontrada")
    return serie.episodios

# UPDATE
@router.patch("/{serie_id}", response_model=Serie)
def atualizar_serie(serie_id: int, dados_novos: Serie, session: Session = Depends(get_session)):
    serie_db = session.get(Serie, serie_id)
    if not serie_db:
        raise HTTPException(status_code=404, detail="Série não encontrada")
    
    dados = dados_novos.model_dump(exclude_unset=True)
    for key, value in dados.items():
        setattr(serie_db, key, value)
        
    session.add(serie_db)
    session.commit()
    session.refresh(serie_db)
    return serie_db

# DELETE
@router.delete("/{serie_id}")
def deletar_serie(serie_id: int, session: Session = Depends(get_session)):
    serie = session.get(Serie, serie_id)
    if not serie:
        raise HTTPException(status_code=404, detail="Série não encontrada")
    
    try:
        session.delete(serie)
        session.commit()
        return {"message": "Série deletada com sucesso"}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=f"Não é possível deletar a série (verifique episódios ou atores associados): {e}")

# RELACIONAMENTO N:N
@router.post("/{serie_id}/atores/{ator_id}")
def adicionar_ator_a_serie(serie_id: int, ator_id: int, session: Session = Depends(get_session)):
    """Cria a relação entre uma Série e um Ator."""
    serie = session.get(Serie, serie_id)
    ator = session.get(Ator, ator_id)
    
    if not serie or not ator:
        raise HTTPException(status_code=404, detail="Série ou Ator não encontrado")
    
    link_existente = session.exec(
        select(SerieAtor).where(SerieAtor.serie_id == serie_id, SerieAtor.ator_id == ator_id)
    ).first()
    
    if link_existente:
        raise HTTPException(status_code=400, detail="Ator já está nesta série")

    link = SerieAtor(serie_id=serie_id, ator_id=ator_id)
    session.add(link)
    session.commit()
    
    return {"message": f"Ator {ator.nome} adicionado à série {serie.titulo}"}

@router.get("/{serie_id}/atores", response_model=List[Ator])
def listar_atores_da_serie(serie_id: int, session: Session = Depends(get_session)):
    """Lista todos os atores de uma série específica."""
    serie = session.get(Serie, serie_id)
    if not serie:
        raise HTTPException(status_code=404, detail="Série não encontrada")
    return serie.atores