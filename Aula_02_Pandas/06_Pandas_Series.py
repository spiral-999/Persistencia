# FILTRAGEM DE DADOS

# Use a mesma series da 05_Pandas_Series.py, imprimindo apenas as notas > 7.0
# Dica: Para filtrar uma series, use: "nome_series <operador> valor" como argumento
# do colchete da series original (nome_series)

import pandas as pd

notas = pd.Series([9.3, 7.4, 5.6], 
        index = ["Matemática", "Biologia", "Geografia"])

print(notas[notas > 7.0])