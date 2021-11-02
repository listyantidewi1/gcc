# A panel is a 3D container of data. The term Panel data is derived from econometrics and is partially responsible for the name pandas − pan(el)-da(ta)-s.

# creating an empty panel
import pandas as pd
import numpy as np

data = {'Item1': pd.DataFrame(np.random.randn(4, 3)),
        'Item2': pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)

# panda panel is not available anymore
