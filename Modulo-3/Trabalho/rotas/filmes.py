from fastapi import APIRouter, HTTPException, Query, status
from beanie import PydanticObjectId, Link
from typing import Optional
from modelos.filme import Filme
from modelos.ator import Ator
from modelos.diretor import Diretor

router = APIRouter(prefix="/filmes", tags=["Filmes"])

@router.post("/", response_model=Filme, status_code=status.HTTP_201_CREATED)
async def criar_filme(filme: Filme):
    await filme.insert()
    return filme

@router.get("/{id}", response_model=Filme)
async def obter_filme(id: PydanticObjectId):
    filme = await Filme.get(id, fetch_links=True)
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme

@router.put("/{id}", response_model=Filme)
async def atualizar_filme(id: PydanticObjectId, dados: dict):
    filme = await Filme.get(id)
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    
    dados_limpos = {k: v for k, v in dados.items() if v is not None}
    
    await filme.set(dados_limpos)
    return filme

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_filme(id: PydanticObjectId):
    filme = await Filme.get(id)
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    await filme.delete()
    return None

@router.get("/", response_model=list[Filme])
async def listar_filmes(
    titulo: str | None = Query(None, description="Busca textual parcial (case-insensitive)"),
    genero: str | None = None,
    ano: int | None = None,
    ano_min: int | None = None,
    ordenar_por: str = Query("titulo", enum=["titulo", "ano", "nota"]),
    direcao: str = Query("asc", enum=["asc", "desc"]),
    offset: int = 0,
    limit: int = 10
):
    query = Filme.find_all(fetch_links=True)

    if titulo:
        query = query.find({"titulo": {"$regex": titulo, "$options": "i"}})
    
    if genero:
        query = query.find(Filme.genero == genero)
    
    if ano:
        query = query.find(Filme.ano == ano)
    if ano_min:
        query = query.find(Filme.ano >= ano_min)

    sort_symbol = "+" if direcao == "asc" else "-"
    query = query.sort(f"{sort_symbol}{ordenar_por}")

    return await query.skip(offset).limit(limit).to_list()

@router.post("/{filme_id}/atores/{ator_id}")
async def adicionar_ator_ao_filme(filme_id: PydanticObjectId, ator_id: PydanticObjectId):
    filme = await Filme.get(filme_id)
    ator = await Ator.get(ator_id)
    
    if not filme or not ator:
        raise HTTPException(status_code=404, detail="Filme ou Ator não encontrado")
    
    for link in filme.atores:
        if link.ref.id == ator.id:
            raise HTTPException(status_code=409, detail="Ator já está neste filme")
        
    filme.atores.append(ator)
    await filme.save()
    return {"mensagem": f"Ator {ator.nome} adicionado ao filme {filme.titulo}"}

@router.get("/stats/contagem-genero")
async def contar_filmes_por_genero():
    pipeline = [
        {"$group": {"_id": "$genero", "total": {"$sum": 1}}},
        {"$sort": {"total": -1}}
    ]
    return await Filme.get_motor_collection().aggregate(pipeline).to_list(None)