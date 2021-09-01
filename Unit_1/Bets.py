import pandas as pd


# header = None — загрузить без строки с заголовком,
# skiprows=n — пропустить n строк (часто у документов бывает техническая «шапка»),
# encoding — загрузить в конкретной кодировке,
# na_values — список значений, который нужно заменить на NaN (специальный объект, обозначающий пропущенное значение).

'''sample = pd.read_csv("sample.csv", sep=',')
columns = sample.columns = ['Name', 'City', 'Age', 'Profession']
columns = sample.columns = ['name', 'city', 'age', 'profession']
# print(columns.lower())
print(sample)'''

log = pd.read_csv("log.csv", sep=',', header=None)
columns = log.columns = ['user_id', 'time', 'bet', 'win']
small_df = log[log.columns[0:9]]
print(small_df.head(10))

