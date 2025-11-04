import pandas as pd
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    categoria: str
    preco: float

class Produto(ProdutoBase):
    id: int

colunas = ["id", "nome", "categoria", "preco"]

dados_iniciais = [
    {"id": 1, "nome": "Teclado Mecânico", "categoria": "Periféricos", "preco": 350.00},
    {"id": 2, "nome": "Monitor Ultrawide", "categoria": "Monitores", "preco": 1800.50}
]

db = pd.DataFrame(dados_iniciais, columns=colunas)

proximo_id = 3

app = FastAPI(
    title="API CRUD de Produtos",
    description="Exercício da Atividade em Sala 01"
)


@app.post("/produtos", response_model=Produto, status_code=status.HTTP_201_CREATED)
def cadastrar_produto(produto: ProdutoBase):
    
    global proximo_id, db
    
    novo_produto = produto.model_dump()
    novo_produto['id'] = proximo_id
    
    db = pd.concat(
        [db, pd.DataFrame([novo_produto])], 
        ignore_index=True
    )
    
    proximo_id += 1
    
    return novo_produto

@app.get("/produtos", response_model=list[Produto]) 
def retornar_todos_produtos():
    
    return db.to_dict('records')

@app.get("/produtos/{id}", response_model=Produto)
def retornar_produto_por_id(id: int):
    
    produto = db[db['id'] == id]
    
    if produto.empty:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Produto com id {id} não encontrado"
        )
    
    return produto.to_dict('records')[0]

@app.put("/produtos/{id}", response_model=Produto)
def atualizar_produto(id: int, produto_atualizado: ProdutoBase):
    
    global db
    
    indice = db.index[db['id'] == id].tolist()
    
    if not indice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Produto com id {id} não encontrado"
        )
        
    idx = indice[0]

    db.loc[idx, 'nome'] = produto_atualizado.nome
    db.loc[idx, 'categoria'] = produto_atualizado.categoria
    db.loc[idx, 'preco'] = produto_atualizado.preco
    
    produto_atualizado_completo = db.loc[idx].to_dict()
    return produto_atualizado_completo

@app.delete("/produtos/{id}")
def remover_produto(id: int):
    
    global db
    
    indice = db.index[db['id'] == id].tolist()
    
    if not indice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Produto com id {id} não encontrado"
        )
    
    idx = indice[0]
    
    db = db.drop(idx).reset_index(drop=True)
    
    return {"message": "Produto removido com sucesso"}