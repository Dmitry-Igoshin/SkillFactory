import pandas as pd
# import numpy as np


ratings = pd.read_csv('c:/Users/Дмитрий/PycharmProjects/ratings.csv')
print(ratings.head())

# userId — идентификатор пользователя, который поставил фильму оценку
# movieId — идентификатор фильма
# rating — выставленная оценка
# timestamp — время (в формате unix time), когда была выставлена оценка

movies = pd.read_csv('c:/Users/Дмитрий/PycharmProjects/movies.csv')
print(movies.head())

# movieId — идентификатор фильма
# title — название фильма
# genres — список жанров, к которым относится фильм

print(ratings.rating.max())
print(ratings.rating.min())

# У датафреймов ratings и movies есть общий столбец movieId. Значит, мы можем объединить эти датафреймы в одну таблицу.
# Используем метод merge:
joined = ratings.merge(movies, on='movieId', how='left')
print(joined.head())
# Схематично метод merge можно описать так:
# joined = left_df.merge(right_df, on='', how='')
print(len(ratings) == len(joined))
