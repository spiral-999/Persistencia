from fastapi import APIRouter, HTTPException, Query, status
from beanie import PydanticObjectId
from modelos.episodio import Episodio
from modelos.serie import Serie

router = APIRouter(prefix="/episodios", tags=["Episódios"])

@router.post("/", response_model=Episodio, status_code=status.HTTP_201_CREATED)
async def criar_episodio(episodio: Episodio):
    if episodio.serie:
        serie = await Serie.get(episodio.serie.ref.id)
        if not serie:
             raise HTTPException(status_code=404, detail="Série não encontrada")
    
    await episodio.insert()
    return episodio

@router.get("/", response_model=list[Episodio])
async def listar_episodios(
    serie_id: str | None = None,
    offset: int = 0,
    limit: int = 10
):
    query = Episodio.find_all(fetch_links=True)
    if serie_id:
        query = query.find({"serie.$id": PydanticObjectId(serie_id)})  
    return await query.skip(offset).limit(limit).to_list()