import pandas as pd
# import numpy as np

''' Метод	        Статистический параметр
    .describe()     Полное описание
    .max()  	    Максимум
    .min()	        Минимум
    .mean()	        Среднее значение
    .sum()	        Сумма
    .count()	    Количество непустых элементов
    .std()	        Стандартное отклонение          '''

football = pd.read_csv('c:/Users/Дмитрий/PycharmProjects/data_sf.csv')
'''with pd.option_context('display.max_rows', None, 'display.max_columns', None):
   print(football.describe())'''

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

football_8 = football[football.columns[1:8]]
s_2 = football['Club'].value_counts()
print(s_2)
print(len(s_2.index))

# Данные об игроках каких позиций (Position) занимают более 10% датасета?
s_3 = football['Position'].value_counts(normalize=True)
print(s_3)

# В каких пределах находятся худшие 20% показателей точности ударов ногой (FKAccuracy)?
s_4 = football['FKAccuracy'].value_counts(bins=5)
print(s_4)

# Переменная result будет содержать количество видов позиций (Position),
# которые занимают игроки, представленные в датасете
# result = len(football['Position'].unique())           # количество видов позиций
result = football['Position'].nunique()               # количество видов позиций
# result = football['Position'].count()
# result = len(football['Position'].value_counts())     # количество видов позиций
print(result)

# У какого процента испанских футболистов (Nationality = 'Spain') зарплата (Wage) находится в пределах
# 25% минимума от наблюдаемого уровня зарплат среди испанских игроков? Ответ дайте в виде целого числа
# (округлите полученный результат) без знака %
Spain = football[football.Nationality == 'Spain'].reset_index()
# number = Spain['Name'].nunique()                        # количество уникальных имен испанских футболистов
number = Spain['Name'].count()                           # количество испанских футболистов
print(number)
Spain_Wage_4 = Spain['Wage'].value_counts(bins=4)       # разбиение испанских футболистов на 4 группы по зарплате
# количество игроков в 1-й (0-й) группе
Spain_Wage_4_0 = Spain[Spain['Wage'] < Spain_Wage_4.index[1].left].index.nunique()
print(Spain_Wage_4_0)
print(Spain_Wage_4_0/number)                            # доля игроков в 1-й (0-й) группе
# print(Spain['Wage'] > Spain_Wage_4.index[3].left)       # попадает ли з/п испан. ф-та в 4-ю гр. среди испан. ф-тов
# print(Spain)                                            # печать д/ф испанских футболистов

# Укажите количество национальностей (Nationality), к которым относятся футболисты,
# выступающие за клуб (Club) "Manchester United"
MU = football[football.Club == 'Manchester United'].reset_index()   # д/ф игроков 'Manchester United'
print(MU)
number_Name = MU['Name'].nunique()                          # количество игроков из МЮ
print(number_Name)
number_Nation = MU['Nationality'].nunique()                 # количество нац-й в МЮ
print(number_Nation)

# С помощью функции unique определите двух футболистов из Бразилии (Nationality = 'Brazil'), выступающих
# за клуб (Club) 'Juventus'. Перечислите их имена (Name, как в датафрейме) через запятую в алфавитном порядке
Juve = football[football.Club == 'Juventus'].reset_index()   # д/ф игроков 'Juventus'
print(Juve[Juve.Nationality == 'Brazil'])

# Укажите, какой из клубов (Club) насчитывает большее количество футболистов возрастом (Age) старше 35 лет
Nagoya_Grampus = football[(football.Club == 'Nagoya Grampus') & (football.Age > 35)]
print(Nagoya_Grampus['Name'].count())
Club_Atlético_Huracán = football[(football.Club == 'Club Atlético Huracán') & (football.Age > 35)]
print(Club_Atlético_Huracán['Name'].count())
LA_Galaxy = football[(football.Club == 'LA Galaxy') & (football.Age > 35)]
print(LA_Galaxy['Name'].count())

# С помощью функции value_counts с параметром bins разбейте всех футболистов родом из Аргентины (Nationality =
# 'Argentina') на 4 равные группы по возрасту. Сколько футболистов из Аргентины в возрасте от 34,75 до 41 года?
Argentina = football[football.Nationality == 'Argentina'].reset_index()
Argentina_Age_4 = Argentina['Age'].value_counts(bins=4)
print(Argentina_Age_4)

# Сколько процентов футболистов из Испании (Nationality = 'Spain') имеют возраст (Age) 21 год?
# Введите с точностью до 2 знаков после запятой без указания знака % (например, 12.35)
Spain_Age = Spain['Age'].value_counts(normalize=True)
print(Spain_Age)

# Мы передали в функцию groupby на вход колонку (или список колонок), по которой будет осуществляться группировка.
# Это объект группировки, он хранит в себе информацию о том, какие строки датафрейма (по индексным номерам)
# соответствуют определенной группе (в нашем случае определенному клубу) Вызваваем у объекта группировки атрибут groups:
print(football.groupby(['Club']).groups)
grouped_df = football.groupby(['Club']).sum()
print(grouped_df)
print(grouped_df.loc['Ajax'])
print(grouped_df.loc['Ajax']['Wage'])
grouped_df = football.groupby(['Club'])['Wage'].sum()
print(grouped_df)
grouped_df = football.groupby(['Club'])['Wage'].sum().sort_values(ascending=False)      # По убыванию
# grouped_df = football.groupby(['Club'])['Wage'].sum().sort_values(ascending=True)     # По возрастанию
print(grouped_df.head(5))

# Отметьте позиции (Position), по которым общая сумма зарплат (Wage) игроков превышает 5 млн евро в год
grouped_df = football.groupby(['Position'])['Wage'].sum().sort_values(ascending=False)      # По убыванию
print(grouped_df.head(10))

# сгруппируем игроков по национальностям (Nationality) и посчитаем среднюю зарплату,  средний возраст и
# среднюю силу удара
print(football.groupby(['Nationality'])[['Wage','Age','ShotPower']].mean())
print(football.groupby(['Nationality'])[['Wage','Age','ShotPower']].mean().sort_values(['Wage'],ascending=False).head(10))
print(football.loc[football['Nationality'] == 'Dominican Republic'][['Name','Club','Wage','Age','ShotPower']])

# Посчитайте среднюю зарплату (Wage) и цену (Value) игроков разных позиций (Position).
# Представители какой позиции имеют самую высокую среднюю ценность?
print(football.groupby(['Position'])[['Wage','Value']].mean().sort_values(['Value'],ascending=False))
