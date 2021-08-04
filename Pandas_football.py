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

football = pd.read_csv('c:/Users/Дмитрий/PycharmProjects/data_sf.csv')
# print(football)
# print(football.head())
# print(football.tail())
# print(football.mean())
# print(football.info(memory_usage = 'deep'))
# print(football.describe(include=['int64']))            # , 'object'

# print(football.Age)
# print(football[football.Age > 40])
# print(football[football.Age > football.Age.mean()])
# print(football[(football.Age < football.Age.mean()) | (football.Club == 'FC Barcelona')])
# print(football[(football.Age < football.Age.mean()) & (football.Club == 'FC Barcelona')].Wage.mean())
# print(football[(football.Wage > football.Wage.mean())].SprintSpeed.mean())
# print(football[(football.Wage < football.Wage.mean())].SprintSpeed.mean())
print(football[(football.Wage < football.Wage.mean())].SprintSpeed.mean())
# print()
# print()

'''with pd.option_context('display.max_rows', None, 'display.max_columns', None):
   print(football.describe())'''

