from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from typing import List, Optional
from database import get_session
from modelos.episodio import Episodio
from modelos.serie import Serie

router = APIRouter(prefix="/episodios", tags=["Episódios"])

@router.post("/", response_model=Episodio, status_code=201)
def criar_episodio(episodio: Episodio, session: Session = Depends(get_session)):
    if not session.get(Serie, episodio.serie_id):
        raise HTTPException(status_code=404, detail="Série informada não encontrada")
        
    session.add(episodio)
    session.commit()
    session.refresh(episodio)
    return episodio

@router.get("/", response_model=List[Episodio])
def listar_episodios(
    session: Session = Depends(get_session),
    serie_id: Optional[int] = Query(None, description="Filtrar por ID da série"),
    temporada: Optional[int] = Query(None, description="Filtrar por temporada")
):
    query = select(Episodio)
    if serie_id:
        query = query.where(Episodio.serie_id == serie_id)
    if temporada:
        query = query.where(Episodio.temporada == temporada)
        
    return session.exec(query).all()

@router.get("/{episodio_id}", response_model=Episodio)
def obter_episodio(episodio_id: int, session: Session = Depends(get_session)):
    episodio = session.get(Episodio, episodio_id)
    if not episodio:
        raise HTTPException(status_code=404, detail="Episódio não encontrado")
    return episodio

@router.delete("/{episodio_id}")
def deletar_episodio(episodio_id: int, session: Session = Depends(get_session)):
    episodio = session.get(Episodio, episodio_id)
    if not episodio:
        raise HTTPException(status_code=404, detail="Episódio não encontrado")
    
    session.delete(episodio)
    session.commit()
    return {"message": "Episódio removido com sucesso"}