import pandas as pd


ratings = pd.read_csv('ratings_example.txt', sep='\t')
print(ratings.head())

movies = pd.read_csv('movies_example.txt', sep='\t')
print(movies.head())

# joined = ratings.merge(movies, on='movieId', how='left')
# joined = ratings.merge(movies, on='movieId', how='right')
# joined = ratings.merge(movies, on='movieId', how='inner')
# joined = ratings.merge(movies, on='movieId', how='outer')
# print(joined.head())

# Метод drop_duplicates позволяет удалить дубликаты из таблицы movies.
# В параметре subset указываем один или несколько столбцов, по комбинации которых хотим удалить дубликаты.
# С помощью параметра keep указываем, какой из встречающихся дубликатов оставить (например, первый или последний).
# Параметр inplace указ-т, что измен-я нужно сохр-ть в д/ф, к к-му прим-ся метод (в нашем случае — в д/фр movies):
movies.drop_duplicates(subset='movieId', keep='first', inplace=True)
movies.head()
# joined = ratings.merge(movies, how='left', on='movieId')
# print(joined.head())
print(ratings.merge(movies, how='left', on='movieId'))
