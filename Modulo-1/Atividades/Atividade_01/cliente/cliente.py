import httpx

BASE_URL = "http://127.0.0.1:8000"

def main():
    print("--- Iniciando Testes da API de Produtos com HTTPOX ---")

    try:
        print("\n[TESTE] POST /produtos (Cadastrando 3 produtos)")
        produto3 = {"nome": "Notebook Gamer", "categoria": "Eletrônicos", "preco": 5999.90}
        produto4 = {"nome": "Mouse Óptico", "categoria": "Acessórios", "preco": 120.50}
        produto5 = {"nome": "Cadeira de Escritório", "categoria": "Móveis", "preco": 899.00}
        
        r1 = httpx.post(f"{BASE_URL}/produtos", json=produto3)
        print(f"Produto 3 (ID: {r1.json()['id']}) cadastrado.")
        
        r2 = httpx.post(f"{BASE_URL}/produtos", json=produto4)
        print(f"Produto 4 (ID: {r2.json()['id']}) cadastrado.")
        
        r3 = httpx.post(f"{BASE_URL}/produtos", json=produto5)
        print(f"Produto 5 (ID: {r3.json()['id']}) cadastrado.")

        print("\n[TESTE] GET /produtos (Listando todos)")
        r_get_all = httpx.get(f"{BASE_URL}/produtos")
        print("Status Code:", r_get_all.status_code)
        print(r_get_all.json()) 

        print("\n[TESTE] GET /produtos/2 (Buscando ID 2 - Pré-cadastrado)")
        id_buscar = 2
        r_get_one = httpx.get(f"{BASE_URL}/produtos/{id_buscar}")
        print("Status Code:", r_get_one.status_code)
        print(r_get_one.json())
        
        print("\n[TESTE] PUT /produtos/2 (Atualizando ID 2)")
        id_atualizar = 2
        dados_atualizados = {"nome": "Monitor Ultrawide 49p", "categoria": "Monitores Premium", "preco": 2500.00}
        
        r_put = httpx.put(f"{BASE_URL}/produtos/{id_atualizar}", json=dados_atualizados)
        print("Status Code:", r_put.status_code)
        print("Dados atualizados:")
        print(r_put.json())
        
        print(f"\n[TESTE] GET /produtos/{id_atualizar} (Verificando atualização)")
        r_get_check = httpx.get(f"{BASE_URL}/produtos/{id_atualizar}")
        print(r_get_check.json()) 

        print("\n[TESTE] DELETE /produtos/1 (Removendo ID 1 - Pré-cadastrado)")
        id_remover = 1
        r_delete = httpx.delete(f"{BASE_URL}/produtos/{id_remover}")
        print("Status Code:", r_delete.status_code)
        print(r_delete.json()) 

        print("\n[TESTE] GET /produtos (Listando todos após remoção)")
        r_get_final = httpx.get(f"{BASE_URL}/produtos")
        print(r_get_final.json()) 
        
        print("\n[TESTE] GET /produtos/999 (Testando 404 Not Found)")
        id_inexistente = 999
        r_get_404 = httpx.get(f"{BASE_URL}/produtos/{id_inexistente}")
        print("Status Code:", r_get_404.status_code)
        print(r_get_404.json()) 
        
    except httpx.ConnectError:
        print("\n[ERRO] Não foi possível conectar ao servidor.")
        print(f"Por favor, verifique se o 'main.py' está rodando em {BASE_URL}")

if __name__ == "__main__":
    main()