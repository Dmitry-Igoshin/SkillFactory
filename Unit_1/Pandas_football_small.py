import pandas as pd

football = pd.read_csv('c:/Users/Дмитрий/PycharmProjects/data_sf.csv')

# Возьмем небольшой фрагмент из исходного датафрейма:
small_df = football[football.columns[1:8]].head(25)
print(small_df)

# функция value_counts подсчитывает для каждого значения в серии количество раз, которое это значение встречается.
# Функция value_counts возвращает серию.

# Сколько раз каждая из национальностей встречается в столбце (в серии) Nationality
s = small_df['Nationality'].value_counts()
print(s)
print(s.index)
print(len(s.index))
print(s.values)
print(s['Germany'])
print(s.loc[s > 1])
s_01 = small_df['Nationality'].value_counts(normalize=True)
s_02 = small_df['Age'].value_counts()

# Параметр bins позволяет сгруппировать данные не по категориальному, а по численному признаку (например, по возрасту)
small_df = football[football.columns[0:7]].head(25)
print(small_df)
s_03 = small_df['Wage'].value_counts(bins=4)
print(s_03)
print(s_03.index)
print(s_03.index[3].left)
print(s_03.index[3].right)
print(small_df['Wage'] > s_03.index[3].left)
s_04 = small_df.loc[(small_df['Wage'] > s_03.index[3].left) & (small_df['Wage'] <= s_03.index[3].right)]
print(s_04)

# количество уникальных национальностей
print(small_df['Nationality'].unique())
print(small_df['Nationality'].nunique())

# преобразовать серию, получившуюся в результате работы функции value_counts, в датафрейм
s = small_df['Nationality'].value_counts()                      # получим серию с количеством значений
s_df = s.reset_index()                                          # создадим новый датафрейм
s_df.columns = ['Nationality','Players Count']                  # переименуем столбцы получившегося датафрейма
print(s_df)
