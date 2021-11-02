import pandas as pd
data = pd.read_csv('input.csv')

# Use the multi-axes indexing funtion
print(data.loc[2:6, ['salary', 'name']])
