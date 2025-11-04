# Crie uma series com os seguintes dados
# ["10", "20", "30", "40", "50"]
# Converta o tipo de dados das Series para númerico ("int32")
# Calcule a média dos valores
# Dica: Use o método Series.astype("int32") para converter todos os elementos
import pandas as pd

series = pd.Series(["10", "20", "30", "40", "50"])
series = series.astype("int32") # converte o tipo de dado das Series para inteiro
media = series.mean() # .mean() calcula a média dos valores da series
print("Média : ", media)