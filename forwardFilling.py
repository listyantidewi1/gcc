import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
                                                'h'], columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print(df.fillna(method='pad'))

# Using the concepts of filling discussed in the ReIndexing Chapter we will fill the missing values.

# Method	        Action
# pad/fill	        Fill methods Forward
# bfill/backfill	Fill methods Backward
