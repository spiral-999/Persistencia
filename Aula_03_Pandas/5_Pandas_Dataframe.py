# Crie um Dataframe com os seguintes dados:

# Nome      Idade       Cidade
# Ana       23          São Paulo
# Bruno     30          Rio de Janeiro
# Carlos    27          Curitiba
# Diana     22          Belo Horizonte

import pandas as pd
pessoas_df = pd.read_csv("../Persistencia/Aula_03_Pandas/pessoas.csv")

# Exibir apenas as coluna "Nome"
print(pessoas_df["Nome"])


# Exibir as colunas "Nome" e "Cidade"
print(pessoas_df["Nome", "Cidade"])