from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from database import get_session
from modelos.diretor import Diretor

router = APIRouter(prefix="/diretores", tags=["Diretores"])

@router.post("/", response_model=Diretor)
def criar_diretor(diretor: Diretor, session: Session = Depends(get_session)):
    session.add(diretor)
    session.commit()
    session.refresh(diretor)
    return diretor

@router.get("/", response_model=List[Diretor])
def listar_diretores(session: Session = Depends(get_session)):
    query = select(Diretor)
    resultados = session.exec(query).all()
    return resultados

@router.get("/{diretor_id}", response_model=Diretor)
def obter_diretor(diretor_id: int, session: Session = Depends(get_session)):
    diretor = session.get(Diretor, diretor_id)
    if not diretor:
        raise HTTPException(status_code=404, detail="Diretor não encontrado")
    return diretor