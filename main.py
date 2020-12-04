import pandas as pd
import numpy as np

df = pd.read_csv('transactions.csv', sep=',')
print(df[df.STATUS == 'OK'].sort_values(by = 'SUM').tail(3))
print(df[df.CONTRACTOR == 'Umbrella, Inc'][df.STATUS == 'OK'].sum().T['SUM'])