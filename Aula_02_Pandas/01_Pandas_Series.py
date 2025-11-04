import pandas as pd

# Série não rotulada(sem labels)
# notas = pd.Series([7.5, 4.6, 9.2, 5.5])

notas = pd.Series(
    [7.5, 4.6, 9.2, 5.5], 
    index = ["João", "Marcelo", "Maria", "Thaís"]
)

# Depreciado
#print(notas[2])

# Forma atual
#print(notas.iloc[2])

# Forma pelo label
try:
    print(notas["Marcelo"])
except KeyError as e:
    print("Ocorreu uma execeção : ", type(e).__name__)