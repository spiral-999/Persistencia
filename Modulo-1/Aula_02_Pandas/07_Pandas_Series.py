# Seja a series:

# São Paulo: 12.3 Milhões de habitantes
# Rio de Janeiro: 6.7 Milhões de habitantes
# Salvador: 2.9 Milhões de habitantes

# Adicione a cidade de Belo Horizonte(2.5) e remova a cidade de Salvador
# Dica: Para adicionar, você atribui um valor a uma nova chave via colchetes
# Para remover, use "series.drop(LABEL)" / Atribuições não modificam a Series

import pandas as pd

cidades = pd.Series(
    [12.3, 6.7, 2.9], 
    index = ["São Paulo", "Rio de Janeiro", "Salvador"]
)

# cidades.loc["Belo Horizonte"] = 2.5
cidades["Belo Horizonte"] = 2.5 # adiciona o novo elemento e seu index na Series

cidades = cidades.drop("Salvador") # remove o elemento da Series
print(cidades)
