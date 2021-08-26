''' Метод	        Статистический параметр
    .describe()     Полное описание
    .max()  	    Максимум
    .min()	        Минимум
    .mean()	        Среднее значение
    .sum()	        Сумма
    .count()	    Количество непустых элементов
    .std()	        Стандартное отклонение          '''

import pandas as pd
# import numpy as np

# data = pd.Series(list(range(10, 1001)))
# print(data.loc[10] + data.loc[23] - data.loc[245] + data.iloc[122])

'''
# df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df = pd.DataFrame([[1, 2, 3], [2, 3, 4]],
                  columns=['foo', 'bar', 'baz'],
                  index=['foobar', 'foobaz'])
print(df)
'''

df = pd.DataFrame([[i, i+1.2, i+2, 'hi'] for i in range(10)],
                  columns=['foo', 'bar', 'baz', 'foobar'])
print(df)
print(df.mean())
print(df['foo'])
print(df.bar)
