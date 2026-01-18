from fastapi import APIRouter, HTTPException, Query, status
from beanie import PydanticObjectId
from modelos.ator import Ator
from modelos.filme import Filme

router = APIRouter(prefix="/atores", tags=["Atores"])

@router.post("/", response_model=Ator, status_code=status.HTTP_201_CREATED)
async def criar_ator(ator: Ator):
    await ator.insert()
    return ator

@router.get("/", response_model=list[Ator])
async def listar_atores(
    nome: str | None = Query(None, description="Busca por nome"),
    offset: int = 0,
    limit: int = 10
):
    query = Ator.find_all()
    if nome:
        query = query.find({"nome": {"$regex": nome, "$options": "i"}})
    return await query.skip(offset).limit(limit).to_list()

@router.get("/{id}", response_model=Ator)
async def obter_ator(id: PydanticObjectId):
    ator = await Ator.get(id)
    if not ator:
        raise HTTPException(status_code=404, detail="Ator não encontrado")
    return ator

@router.put("/{id}", response_model=Ator)
async def atualizar_ator(id: PydanticObjectId, dados: dict):
    ator = await Ator.get(id)
    if not ator:
        raise HTTPException(status_code=404, detail="Ator não encontrado")
    dados = {k: v for k, v in dados.items() if v is not None}
    await ator.set(dados)
    return ator

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_ator(id: PydanticObjectId):
    ator = await Ator.get(id)
    if not ator:
        raise HTTPException(status_code=404, detail="Ator não encontrado")
    await ator.delete()
    return None

@router.get("/{id}/filmes")
async def listar_filmes_do_ator(id: PydanticObjectId):
    filmes = await Filme.find(
        {"atores.$id": id}, 
        fetch_links=True
    ).to_list()
    return filmes