# pip install fastapi uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

# iniciar o aplicativo (API) uvicorn main:app --reload
app = FastAPI()

contador_id = 1
alunos_df = pd.DataFrame(columns=["id", "nome", "curso", "IRA"])

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