import requests

BASE_URL = "http://127.0.0.1:8000"

def adicionar_aluno(nome, nota):
    print(f"Adicionando o Aluno : {nome} com nota {nota}")
    response = requests.post(f"{BASE_URL}/alunos", params={"nome": nome, "nota": nota})
    if response.status_code == 200:
        print("Resposta do servidor:", response.json())
    else:
        print(f"Erro ao adicionar: {response.status_code}")

def obter_nota(nome):
    print(f"Obtendo Nota do Aluno : {nome}")
    response = requests.get(f"{BASE_URL}/alunos/{nome}")
    if response.status_code == 200:
        print("Resposta do servidor:", response.json())
    elif response.status_code == 404:
        print("Resposta do servidor (Erro 404):", response.json())
    else:
        print(f"Erro ao buscar: {response.status_code}")

def listar_alunos():
    print("\nTentando listar TODOS os alunos...")
    response = requests.get(f"{BASE_URL}/alunos")
    if response.status_code == 200:
        print("Resposta do servidor (Todos os alunos):")
        lista_de_alunos = response.json()
        print(lista_de_alunos)
    else:
        print(f"Erro ao listar: {response.status_code}")

if __name__ == "__main__":
    try:
        adicionar_aluno("Novo Aluno 1", 4.5)
        adicionar_aluno("Novo Aluno 2", 2.2)
        adicionar_aluno("Novo Aluno 3", 5.9)
        adicionar_aluno("Novo Aluno 4", 6.2)
        adicionar_aluno("Novo Aluno 5", 1.6)
        listar_alunos()
        obter_nota("Mateus")
        obter_nota("Novo Aluno 4")
        adicionar_aluno("Aluno Intercambio", 9.8) 
        listar_alunos()
        obter_nota("Novo Aluno 7")

    except requests.exceptions.ConnectionError:
        print(f"Certifique-se que o servidor está ativo em {BASE_URL}")