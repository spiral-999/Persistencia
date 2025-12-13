from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from datetime import datetime, date # Importação necessária
from database import get_session
from modelos.ator import Ator

router = APIRouter(prefix="/atores", tags=["Atores"])

@router.post("/", response_model=Ator)
def criar_ator(ator: Ator, session: Session = Depends(get_session)):
    # CORREÇÃO DE SEGURANÇA:
    # Se a data chegou como string, forçamos a conversão para objeto date do Python
    if isinstance(ator.data_nascimento, str):
        ator.data_nascimento = datetime.strptime(ator.data_nascimento, "%Y-%m-%d").date()
    
    session.add(ator)
    session.commit()
    session.refresh(ator)
    return ator

@router.get("/", response_model=List[Ator])
def listar_atores(session: Session = Depends(get_session)):
    query = select(Ator)
    resultados = session.exec(query).all()
    return resultados

@router.get("/{ator_id}", response_model=Ator)
def obter_ator(ator_id: int, session: Session = Depends(get_session)):
    ator = session.get(Ator, ator_id)
    if not ator:
        raise HTTPException(status_code=404, detail="Ator não encontrado")
    return ator