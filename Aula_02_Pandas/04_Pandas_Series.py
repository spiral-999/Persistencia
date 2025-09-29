# Exercício 01
# Crie uma Series chamada precos_frutas com o preço de 3 frutas:
# Maça: 2.50 
# Banana: 5.60
# Abacate: 6.30
# Imprima o preço da Banana usando a chave
# Depois imprima o mesmo preço usando a função series.iloc[pos]

import pandas as pd

frutas = pd.Series([2.50, 5.60, 6.30], 
                  index = ["Maça", "Banana", "Abacate"])

print("Usando a forma depreciada:")
print(frutas[2])

print("Usando a forma atual(iloc):  ")
print(frutas.iloc[2])

print("Usando o label: ")
print(frutas["Banana"])