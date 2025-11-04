# Crie uma Series com as seguintes notas do aluno:

# Matemática: 9.3
# Biologia: 7.4
# Geografia: 5.6

# Em seguida, você deve ADICIONAR 0.5 a TODAS as notas de uma vez
# Imprima a nova series

# Dica: Para somar em uma Series, use a função series.add(valor).
# Lembre-se: Essa operação NÃO modifica a Series original, mas sim gera uma nova

import pandas as pd

notas = pd.Series(
    [9.3, 7.4, 5.6], 
    index = ["Matemática", "Biologia", "Geografia"]
)

print("Notas Originais: ")
print(notas)

print("------------------")

notas_extra = notas.add(0.5) # adiciona a Series, não modifica os valores originais 
print("Notas Somadas: ")
print(notas_extra)


