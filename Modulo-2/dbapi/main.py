import sqlite3

# 1. CONEXÃO (Slide 07, pág 22)
# Cria o arquivo 'exemplo.db' se não existir e abre a conexão.
conn = sqlite3.connect('exemplo.db')

# 2. CURSOR (Slide 07, pág 23)
# O cursor é criado a partir da conexão para executar comandos.
cursor = conn.cursor()

try:
    # 3. EXECUÇÃO DE DDL (Data Definition Language)
    # Cria a tabela. Note que é SQL puro passado como string.
    cursor.execute('CREATE TABLE IF NOT EXISTS alunos (id INT PRIMARY KEY, nome TEXT)')
    
    # 4. PREVENÇÃO DE SQL INJECTION (Slide 07, pág 28)
    # IMPORTANTE: Usa-se '?' como placeholder. NUNCA formate a string com f-strings aqui.
    # A tupla (1, 'Maria') é passada separadamente para o driver sanitizar.
    cursor.execute('INSERT INTO alunos (id, nome) VALUES (?, ?)', (1, 'Maria'))
    cursor.execute('INSERT INTO alunos (id, nome) VALUES (?, ?)', (2, 'João'))
    
    # 5. CONTROLE DE TRANSAÇÃO (Slide 07, pág 22)
    # Nada é salvo no disco até o commit(). Se o programa travar antes, perde-se tudo.
    conn.commit()
    
except Exception as e:
    # Em caso de erro, desfaz qualquer alteração parcial desta transação.
    conn.rollback()
    print(f'Erro: {e}')

# 6. CONSULTA (DQL)
cursor.execute('SELECT * FROM alunos')

# 7. RECUPERAÇÃO DE DADOS (Slide 07, pág 23)
# fetchall() retorna uma lista de tuplas [(1, 'Maria'), (2, 'João')]
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)

# 8. FECHAMENTO (Slide 07, pág 22, 23)
# Libera recursos do sistema.
cursor.close()
conn.close()