import pandas as pd
import numpy as np # pip install numpy

np_array = np.array([10,20,30])
print(np_array[2])
print("----------------------------------")
series = pd.Series(np_array, index = ["A", "B", "C"])
print(series)
print("----------------------------------")
print(series["B"])