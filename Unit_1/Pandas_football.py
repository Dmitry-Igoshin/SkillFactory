import pandas as pd
import numpy as np

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

# Функция nunique, которая позволяет посчитать количество уникальных значений по серии.
# Её лучше всего применять к тем колонкам датафрейма, в которых хранятся категорийные данные:
# print(football.groupby(['Nationality'])[['Club','Name']].nunique())

# Посчитайте среднюю (mean) и медианную (median) зарплату (Wage) футболистов из разных клубов (Club).
# В скольких клубах средняя и медианная зарплаты совпадают?
# Подсказка: чтобы в процессе группировки применить к данным одновременно две агрегирующие функции,
# необходимо указать их как аргументы метода agg:
# df.groupby(столбец_для_группировки)[столбцы_для_отображения].agg(['функция_1', 'функция_2'])
# print(football.groupby(['Club'])['Wage'].median())
Club_median_mean = football.groupby(['Club'])['Wage'].agg(['median','mean']).reset_index()
# переименуем столбцы получившегося датафрейма
Club_median_mean.columns = ['Club','median_Wage','mean_Wage']
# print(Club_median_mean[Club_median_mean.medianWage == Club_median_mean.meanWage].count())
print(Club_median_mean[Club_median_mean.median_Wage == Club_median_mean.mean_Wage].sort_values(['mean_Wage'],ascending=False))

# print(football.groupby(['Club'])['Wage'].apply(lambda x: np.mean(x) == np.median(x)))
# print('123', football.groupby(['Club'])['Wage'].filter(lambda x: np.mean(x) == np.median(x)))

# С помощью функции groupby посчитайте сумму зарплат (Wage) футболистов клуба (Club) "Chelsea"
sum_Wage = football.groupby(['Club'])['Wage'].sum().sort_values(ascending=False)      # По убыванию
print(sum_Wage.loc['Chelsea'])

# Определите максимальную зарплату футболиста национальности (Nationality) Аргентина ("Argentina") в возрасте 20 лет
Argentina_20 = football[(football.Nationality == 'Argentina') & (football.Age == 20)].reset_index()
Argentina_20_max = Argentina_20[Argentina_20.Wage == Argentina_20.Wage.max()]
print(Argentina_20_max.Name, Argentina_20_max.Wage)

# Определите максимальную зарплату футболиста национальности (Nationality) Аргентина ("Argentina") в возрасте 30 лет
Argentina_30 = football[(football.Nationality == 'Argentina') & (football.Age == 30)].reset_index()
Argentina_30_max = Argentina_30[Argentina_30.Wage == Argentina_30.Wage.max()]
print(Argentina_30_max.Name, Argentina_30_max.Wage)
# Определите минимальную зарплату футболиста национальности (Nationality) Аргентина ("Argentina") в возрасте 30 лет
Argentina_30_min = Argentina_30[Argentina_30.Wage == Argentina_30.Wage.min()]
print(Argentina_30_min.Name, Argentina_30_min.Wage)

# Определите максимальную силу (Strength) и баланс (Balance) среди игроков клуба (Club) "FC Barcelona"
# из Аргентины ("Argentina"). Ответ введите через точку с запятой без пробела
Argentina_Barcelona = football[(football.Nationality == 'Argentina') & (football.Club == 'FC Barcelona')].reset_index()
Strength_max = Argentina_Barcelona[Argentina_Barcelona.Strength == Argentina_Barcelona.Strength.max()]
Balance_max = Argentina_Barcelona[Argentina_Barcelona.Balance == Argentina_Barcelona.Balance.max()]
print(Strength_max.Strength, Balance_max.Balance)

# Сводная таблица, показывающая максимальные зарплаты игроков на разных позициях,
# играющих за разные клубы, была создана с помощью кода:
# df2 = football.pivot_table(columns = 'Position', index = 'Club', values = 'Wage', aggfunc = 'max')
# print(df2)
# С помощью какого кода можно получить из этой таблицы информацию о максимальной зарплате вратаря (GK),
# играющего за футбольный клуб "Manchester City"?
# print(df2.loc['Manchester City']['GK'])

# Для того, чтобы заменить NaN на 0, можно применить дополнительный параметр fill_value.
# Этот параметр принимает значение, которым нужно заполнить все NaN в получившейся сводной таблице:
"""pivot = football.loc[football['Club'].isin(['FC Barcelona','Real Madrid','Juventus','Manchester United'])].pivot_table(
values=['Wage'],index=['Nationality'],columns=['Club'],aggfunc='sum',margins=True,fill_value=0)"""
# print(pivot)

# Применим другую агрегирующую функцию count, чтобы посчитать количество футболистов по клубам и национальностям:
"""pivot = football.loc[football['Club'].isin(['FC Barcelona','Real Madrid','Juventus','Manchester United'])].pivot_table(
values=['Name'],index=['Nationality'],columns=['Club'],aggfunc='count',margins=True,fill_value=0)"""
# print(pivot)
# print(pivot.loc['Argentina']['Name']['Manchester United'])

# Создайте сводную таблицу, содержащую сведения о количестве игроков, занимающих разные позиции в каждом клубе.
# Отсутствующие значения замените нулями.
pivot = football.pivot_table(values=['Name'],index=['Position'],columns=['Club'],aggfunc='count',margins=True,fill_value=0)
print(pivot)

# Используя таблицу, созданную на предыдущем шаге, определите, сколько клубов не содержат данных о центральных полузащитниках. (CM)
# Подсказка: для выполнения этого задания желательно сохранить сводную таблицу в виде отдельного датафрейма
# и сгруппировать часть данных этого датафрейма с помощью value_counts()
Position_Club = pivot.reset_index()
print(Position_Club['Club'].value_counts(normalize=True))

