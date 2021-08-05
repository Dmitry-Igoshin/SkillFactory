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

# Какова средняя скорость (SprintSpeed) футболистов, зарплата (Wage) которых выше среднего? Ответ округлите до сотых
print(football[(football.Wage > football.Wage.mean())].SprintSpeed.mean())

# Какова средняя скорость (SprintSpeed) футболистов, зарплата (Wage) которых ниже среднего? Ответ округлите до сотых
print(football[(football.Wage < football.Wage.mean())].SprintSpeed.mean())

# Сколько пенальти (Penalties) забили бразильские (Nationality, Brazil) футболисты за период,
# данные о котором представлены в датасете?
print(football[(football.Nationality == 'Brazil')].Penalties.sum())

# Укажите средний возраст (Age) игроков, у которых точность удара головой (HeadingAccuracy) > 50.
# Ответ округлите до сотых.
print(football[(football.HeadingAccuracy > 50)].Age.mean())

# Укажите возраст (Age) самого молодого игрока, у которого хладнокровие (Composure) и реакция (Reactions)
# превышают 90% от максимального значения, представленного в датасете.
print(football[(football.Composure > 0.9 * football.Composure.max()) &
               (football.Reactions > 0.9 * football.Reactions).max()].Age.min())

# Определите, на сколько средняя реакция (Reactions) самых взрослых игроков (т.е. игроков,
# чей возраст (Age) равен максимальному) больше средней реакции самых молодых игроков. Ответ округлите до сотых.
print(football[(football.Age == football.Age.max())].Reactions.mean()
      -football[(football.Age == football.Age.min())].Reactions.mean())

# Из какой страны (Nationality) происходит больше всего игроков, чья стоимость (Value) превышает среднее значение?
# More_than_mean_Value = football[football.Value > football.Value.mean()]
# print(More_than_mean_Value.Nationality.value_counts().index[0])
print(football[football.Value > football.Value.mean()].Nationality.value_counts().index[0])
print(football[football.Value > football.Value.mean()].Nationality.value_counts().values[0])

# print(")", football[football.Value > football.Value.mean()].groupby("Nationality").Nationality.count().sort_values())

# Определите, во сколько раз средняя зарплата (Wage) голкипера (Position, GK)
# с максимальным значением показателя "Рефлексы" (GKReflexes) выше средней зарплаты голкипера
# с максимальным значением показателя "Владение мячом" (GKHandling). Ответ округлите до сотых.
mean_Wage_1 = football[(football.Position == 'GK') & (football.GKReflexes == football.GKReflexes.max())].Wage.mean()
mean_Wage_2 = football[(football.Position == 'GK') & (football.GKHandling == football.GKHandling.max())].Wage.mean()
print(mean_Wage_1, mean_Wage_2, mean_Wage_1 / mean_Wage_2)

# Определите, во сколько раз средняя сила удара (ShotPower) самых агрессивных игроков
# (игроков с максимальным значением показателя "Агрессивность" (Aggression))
# выше средней силы удара игроков с минимальной агрессией. Ответ округлите до сотых.
mean_ShotPower_1 = football[football.Aggression == football.Aggression.max()].ShotPower.mean()
mean_ShotPower_2 = football[football.Aggression == football.Aggression.min()].ShotPower.mean()
print(mean_ShotPower_1, mean_ShotPower_2, mean_ShotPower_1 / mean_ShotPower_2)

'''with pd.option_context('display.max_rows', None, 'display.max_columns', None):
   print(football.describe())'''

