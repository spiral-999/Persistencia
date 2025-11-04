import pandas as pd

series1 = pd.Series([1,2,3])
series2 = pd.Series([4,5,6])

soma_series = series1.add(series2) # nao modifica a series original
print(soma_series)

# .add() soma todos os elementos de duas series