from fastapi import APIRouter, HTTPException, status
from beanie import PydanticObjectId
from modelos.diretor import Diretor
from modelos.filme import Filme

router = APIRouter(prefix="/diretores", tags=["Diretores"])

@router.post("/", response_model=Diretor, status_code=status.HTTP_201_CREATED)
async def criar_diretor(diretor: Diretor):
    await diretor.insert()
    return diretor

@router.get("/", response_model=list[Diretor])
async def listar_diretores(offset: int = 0, limit: int = 10):
    return await Diretor.find_all().skip(offset).limit(limit).to_list()

@router.get("/{id}", response_model=Diretor)
async def obter_diretor(id: PydanticObjectId):
    diretor = await Diretor.get(id)
    if not diretor:
        raise HTTPException(status_code=404, detail="Diretor não encontrado")
    return diretor

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_diretor(id: PydanticObjectId):
    diretor = await Diretor.get(id)
    if not diretor:
        raise HTTPException(status_code=404, detail="Diretor não encontrado")
    await diretor.delete()
    return None

@router.get("/{id}/filmes")
async def listar_filmes_do_diretor(id: PydanticObjectId):
    return await Filme.find(
        {"diretor.$id": id},
        fetch_links=True
    ).to_list()