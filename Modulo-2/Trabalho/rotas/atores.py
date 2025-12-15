from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from typing import List, Optional
from datetime import datetime
from database import get_session
from modelos.ator import Ator

router = APIRouter(prefix="/atores", tags=["Atores"])

@router.post("/", response_model=Ator, status_code=201)
def criar_ator(ator: Ator, session: Session = Depends(get_session)):
    if isinstance(ator.data_nascimento, str):
        try:
            ator.data_nascimento = datetime.strptime(ator.data_nascimento, "%Y-%m-%d").date()
        except ValueError:
            raise HTTPException(status_code=400, detail="Formato de data inválido. Use YYYY-MM-DD")

    session.add(ator)
    try:
        session.commit()
        session.refresh(ator)
        return ator
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao criar ator: {e}")

# READ com Filtros
@router.get("/", response_model=List[Ator])
def listar_atores(
    session: Session = Depends(get_session),
    nome: Optional[str] = Query(None, description="Filtro por nome (parcial)"),
    offset: int = 0,
    limit: int = 10
):
    query = select(Ator)
    if nome:
        query = query.where(Ator.nome.contains(nome))
        
    return session.exec(query.offset(offset).limit(limit)).all()

# READ por ID
@router.get("/{ator_id}", response_model=Ator)
def obter_ator(ator_id: int, session: Session = Depends(get_session)):
    ator = session.get(Ator, ator_id)
    if not ator:
        raise HTTPException(status_code=404, detail="Ator não encontrado")
    return ator

# UPDATE
@router.patch("/{ator_id}", response_model=Ator)
def atualizar_ator(ator_id: int, dados_novos: Ator, session: Session = Depends(get_session)):
    ator_db = session.get(Ator, ator_id)
    if not ator_db:
        raise HTTPException(status_code=404, detail="Ator não encontrado")
    dados = dados_novos.model_dump(exclude_unset=True)
    if 'data_nascimento' in dados and isinstance(dados['data_nascimento'], str):
         dados['data_nascimento'] = datetime.strptime(dados['data_nascimento'], "%Y-%m-%d").date()

    for key, value in dados.items():
        setattr(ator_db, key, value)
        
    session.add(ator_db)
    session.commit()
    session.refresh(ator_db)
    return ator_db

# DELETE
@router.delete("/{ator_id}")
def deletar_ator(ator_id: int, session: Session = Depends(get_session)):
    ator = session.get(Ator, ator_id)
    if not ator:
        raise HTTPException(status_code=404, detail="Ator não encontrado")
    
    try:
        session.delete(ator)
        session.commit()
        return {"message": "Ator deletado com sucesso"}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao deletar ator: {e}")