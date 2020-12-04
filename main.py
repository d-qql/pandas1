import pandas as pd
import numpy as np

df = pd.read_csv('transactions.csv', sep=',')
maxOK = []

max = max1 = max2 = max3 = 0
for i in df[df.STATUS == 'OK'][['STATUS', 'SUM']].index:

    if int(df.loc[[i], 'SUM']) > max:
        max3 = max2
        max2 = max1
        max1 = i
        max = int(df.loc[[i], 'SUM'])
sum = sum(df[df.CONTRACTOR == 'Umbrella, Inc'][['SUM']][df.STATUS == 'OK'][['SUM']].index)
print(df.loc[[max1], ['CONTRACTOR', 'STATUS', 'SUM']])
print(df.loc[[max2], ['CONTRACTOR', 'STATUS', 'SUM']])
print(df.loc[[max3], ['CONTRACTOR', 'STATUS', 'SUM']])
print('Сумма всех успешных транзакций Umbrella, Inc', sum)
