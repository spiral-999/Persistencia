from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from typing import List, Optional
from database import get_session
from modelos.diretor import Diretor

router = APIRouter(prefix="/diretores", tags=["Diretores"])

# CREATE
@router.post("/", response_model=Diretor, status_code=201)
def criar_diretor(diretor: Diretor, session: Session = Depends(get_session)):
    session.add(diretor)
    try:
        session.commit()
        session.refresh(diretor)
        return diretor
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao criar diretor: {e}")

# READ com filtros
@router.get("/", response_model=List[Diretor])
def listar_diretores(
    session: Session = Depends(get_session),
    nome: Optional[str] = Query(None, description="Filtro por nome (parcial)"),
    offset: int = 0,
    limit: int = 10
):
    query = select(Diretor)
    if nome:
        query = query.where(Diretor.nome.contains(nome))
    
    return session.exec(query.offset(offset).limit(limit)).all()

# READ por ID
@router.get("/{diretor_id}", response_model=Diretor)
def obter_diretor(diretor_id: int, session: Session = Depends(get_session)):
    diretor = session.get(Diretor, diretor_id)
    if not diretor:
        raise HTTPException(status_code=404, detail="Diretor não encontrado")
    return diretor

# UPDATE
@router.patch("/{diretor_id}", response_model=Diretor)
def atualizar_diretor(diretor_id: int, dados_novos: Diretor, session: Session = Depends(get_session)):
    diretor_db = session.get(Diretor, diretor_id)
    if not diretor_db:
        raise HTTPException(status_code=404, detail="Diretor não encontrado")
    
    dados = dados_novos.model_dump(exclude_unset=True)
    for key, value in dados.items():
        setattr(diretor_db, key, value)
        
    session.add(diretor_db)
    session.commit()
    session.refresh(diretor_db)
    return diretor_db

# DELETE
@router.delete("/{diretor_id}")
def deletar_diretor(diretor_id: int, session: Session = Depends(get_session)):
    diretor = session.get(Diretor, diretor_id)
    if not diretor:
        raise HTTPException(status_code=404, detail="Diretor não encontrado")
    
    try:
        session.delete(diretor)
        session.commit()
        return {"message": "Diretor deletado com sucesso"}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=f"Não foi possível deletar (pode haver filmes associados): {e}")