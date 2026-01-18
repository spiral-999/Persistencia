from fastapi import APIRouter, HTTPException, Query, status
from beanie import PydanticObjectId
from modelos.serie import Serie
from modelos.ator import Ator

router = APIRouter(prefix="/series", tags=["Séries"])

@router.post("/", response_model=Serie, status_code=status.HTTP_201_CREATED)
async def criar_serie(serie: Serie):
    await serie.insert()
    return serie

@router.get("/", response_model=list[Serie])
async def listar_series(offset: int = 0, limit: int = 10):
    return await Serie.find_all(fetch_links=True).skip(offset).limit(limit).to_list()

@router.get("/{id}", response_model=Serie)
async def obter_serie(id: PydanticObjectId):
    serie = await Serie.get(id, fetch_links=True)
    if not serie:
        raise HTTPException(status_code=404, detail="Série não encontrada")
    return serie

@router.post("/{serie_id}/atores/{ator_id}")
async def adicionar_ator_serie(serie_id: PydanticObjectId, ator_id: PydanticObjectId):
    serie = await Serie.get(serie_id)
    ator = await Ator.get(ator_id)
    if not serie or not ator:
        raise HTTPException(status_code=404, detail="Não encontrado")
    
    for link in serie.atores:
        if link.ref.id == ator.id:
            raise HTTPException(status_code=409, detail="Ator já está na série")

    serie.atores.append(ator)
    await serie.save()
    return {"mensagem": "Ator adicionado à série"}  