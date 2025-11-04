import httpx

BASE_URL = "http://127.0.0.1:8000"

def criar_aluno():
    resp = httpx.post(
        f"{BASE_URL}/alunos",
        json = {"nome":"Sicrano", "curso": "CC", "IRA":7.5}
    )
    print(resp.json()["mensagem"])
    print(resp.json()["aluno"])

def listar_alunos():
    resp = httpx.get(f"{BASE_URL}/alunos")
    print(resp.json())

def obter_aluno(id):
    resp = httpx.get(f"{BASE_URL}/alunos/{id}")
    print(resp.json())

def atualizar_aluno(id, aluno):
    resp = httpx.put(
        f"{BASE_URL}/alunos/{id}",
        json = {"nome": aluno.get("nome"), "curso": aluno.get("curso"), "IRA": aluno.get("IRA")}
    )
    print(resp.json())

def apagar_aluno(id):
    resp = httpx.delete(f"{BASE_URL}/alunos/{id}")
    return resp.json()
