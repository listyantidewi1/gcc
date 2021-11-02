import pandas as pd
data = pd.read_csv('input.csv')

# Use the multi-axes indexing funtion
print(data.loc[:, ['salary', 'name']])

# : all data
# 0:5 first 5 data
