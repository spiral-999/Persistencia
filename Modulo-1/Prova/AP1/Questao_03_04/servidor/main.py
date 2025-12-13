# 1 - POST /alunos → recebe o nome e a nota de um aluno e armazena esses dados no DataFrame.
#   ● Se o aluno já existir, a nota deve ser atualizada.
#   ● Caso seja um novo aluno, ele deve ser adicionado.
# 2 - GET /alunos/{nome} → recebe o nome do aluno como parâmetro e retorna sua nota, caso o aluno exista no DataFrame.
#   ● Caso o nome não seja encontrado, retorne uma mensagem informando que o aluno não foi registrado.


from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI() #inicioando a fastAPI

alunos_df = pd.DataFrame(
    {
        "nome" : ["Mateus"],
        "nota" : [10]
    }
)

@app.post("/alunos") # questao 3
def adicionar_aluno(nome: str, nota: float):
    global alunos_df
    filtro = alunos_df["nome"] == nome # filtro para o caso de existencia
    aluno_existe = alunos_df[filtro]

    #   ● Se o aluno já existir, a nota deve ser atualizada.
    if not aluno_existe.empty: # checando se existe
        indice = aluno_existe.index[0]
        alunos_df.loc[indice, "nota"] = nota
        return{
            "mensagem" : f"Nota do Aluno {nome} Atualizada com Sucesso!",
            "aluno": {"nome": nome, "nota": nota}
        }
    #   ● Caso seja um novo aluno, ele deve ser adicionado.
    else:
        novo_aluno = {"nome": nome, "nota": nota}
        alunos_df = alunos_df._append(novo_aluno, ignore_index = True)
        return{
            "mensagem" : f"Aluno {nome} Registrado com Sucesso!",
            "aluno": novo_aluno
        }
    
@app.get("/alunos/{nome}") # questao 3
def obter_nota(nome: str):
    global alunos_df
    filtro = alunos_df["nome"] == nome # filtro para o caso de existencia
    aluno = alunos_df[filtro]

    if aluno.empty:
        raise HTTPException(status_code=404, detail=f"Aluno {nome} Não Foi Registrado") #   ● Caso o nome não seja encontrado, retorne uma mensagem informando que o aluno não foi registrado.
    
    nota_aluno = aluno["nota"].iloc[0]
    return{"nome":nome, "nota":nota_aluno}

@app.get("/alunos") # questao 4
def listar_alunos():
    return alunos_df.to_dict(orient="records")