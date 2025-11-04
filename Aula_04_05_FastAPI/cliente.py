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

# execução
criar_aluno()
criar_aluno()
listar_alunos()