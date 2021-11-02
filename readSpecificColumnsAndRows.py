import pandas as pd
data = pd.read_csv('input.csv')

# Use the multi-axes indexing funtion
print(data.loc[[1, 3, 5], ['salary', 'name']])

# data.loc[[rows],[columns]]
