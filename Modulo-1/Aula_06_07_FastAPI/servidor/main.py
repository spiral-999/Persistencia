# pip install fastapi uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

# iniciar o aplicativo (API) uvicorn main:app --reload
app = FastAPI()

contador_id = 1
# alunos_df = pd.DataFrame(columns=["id", "nome", "curso", "IRA"])
alunos_df = pd.DataFrame(
    {
        "id": [1,2,3],
        "nome": ["Jefferson", "Wladmir", "Fábio"],
        "curso": ["CC", "SI", "ES"],
        "IRA": [9.7, 4.6, 7.3]
    }
)

# modelo para a entidade alunos
class Aluno(BaseModel):
    nome : str
    curso : str
    IRA : float

@app.post("/alunos") # serviço de criação de um aluno
def criar_aluno(aluno : Aluno):

    global alunos_df, contador_id

    novo_aluno = {
        "id" : contador_id,
        "nome" : aluno.nome,
        "curso" : aluno.curso,
        "IRA" : aluno.IRA
    }
    alunos_df = alunos_df._append(novo_aluno, ignore_index = True) # forma com o append
    # alunos_df = pd.concat([alunos_df, pd.DataFrame([novo_aluno])], ignore_index = True) # forma com o concat
    contador_id = contador_id + 1
    return{
        "mensagem" : "Aluno criado com sucesso!",
        "aluno" : novo_aluno
    }

@app.get("/alunos") # serviço de listagem de TODOS os alunos
def listar_alunos():
    return alunos_df.to_dict(orient="records")

@app.get("/alunos/{id}") # obter aluno pelo id
def obter_aluno(id: int):
    global alunos_df
    filtro = alunos_df["id"] == id
    aluno = alunos_df[filtro]
    if aluno.empty:
        raise HTTPException(status_code=404, detail=f"Aluno id : {id} não encontrado")
    return aluno.to_dict(orient="records")[0]

@app.put("/alunos/{id}") # atualizar aluno pelo email
def atualizar_aluno(id: int, aluno: Aluno):
    global alunos_df
    aluno_antigo_idx = alunos_df.index[alunos_df["id"] == id]
    if aluno_antigo_idx.empty:
        raise HTTPException(status_code=404, detail=f"Aluno id : {id} não encontrado")
    alunos_df.loc[aluno_antigo_idx, ["nome", "curso", "IRA"]] = [aluno.nome, aluno.curso, aluno.IRA]
    return{
        "mensagem": f"Aluno {id} atualizado com sucesso",
        "aluno" : alunos_df.loc[aluno_antigo_idx].to_dict(orient="records")[0]
    }

@app.delete("/alunos/{id}") # apagar um objeto pelo id
def apagar_aluno(id: int):
    global alunos_df
    aluno_apagar_idx = alunos_df.index[ alunos_df["id"] == id ]
    if aluno_apagar_idx.empty:
        raise HTTPException(status_code=404, detail=f"Aluno id:{id}, não encontrado")
    alunos_df = alunos_df.drop(aluno_apagar_idx).reset_index(drop = True)
    return { "mensagem":  f"Aluno com {id} apagado com sucesso!"}