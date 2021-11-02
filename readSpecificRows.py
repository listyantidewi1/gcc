import pandas as pd
data = pd.read_csv('input.csv')

# Slice the result for first 5 rows
print(data[0:5]['salary'])

# data[0:5] from 0th data to 5th data
