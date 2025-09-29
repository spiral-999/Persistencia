# Crie uma series com os seguintes dados

import pandas as pd

series = pd.Series(["10", "20", "30", "40", "50"])
series.astype("int32")
media = series.mean()
print("Média : ", media)   