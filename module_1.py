import pandas as pd

Movies = pd.read_csv('c:/Users/Дмитрий/PycharmProjects/movie_bd_v5.csv')

# Вопрос 1. У какого фильма из списка самый большой бюджет?
print(Movies[Movies.budget == Movies.budget.max()].original_title)

# Вопрос 2. Какой из фильмов самый длительный (в минутах)?
print(Movies[Movies.runtime == Movies.runtime.max()].original_title)

# Вопрос 3. Какой из фильмов самый короткий (в минутах)?
print(Movies[Movies.runtime == Movies.runtime.min()].original_title)

# Вопрос 4. Какова средняя длительность фильмов?
print(Movies.runtime.mean())

# Вопрос 5. Каково медианное значение длительности фильмов?
print(Movies.runtime.describe())

# Вопрос 6. Какой фильм самый прибыльный?
# Movies.profit = Movies.revenue - Movies.budget
Movies["profit"] = Movies.revenue - Movies.budget
print(Movies[Movies.profit == Movies.profit.max()].original_title)

# Вопрос 7. Какой фильм самый убыточный?
print(Movies[Movies.profit == Movies.profit.min()].original_title)

# Вопрос 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?
print(Movies[Movies.revenue - Movies.budget > 0].value_counts())

# Вопрос 9. Какой фильм оказался самым кассовым в 2008 году?
Movies_2008 = Movies[Movies.release_year == 2008]
print(Movies_2008[Movies_2008.revenue == Movies_2008.revenue.max()].original_title)

# Вопрос 10. Самый убыточный фильм за период с 2012 по 2014 годы (включительно)?
Movies_12_14 = Movies[(Movies.release_year > 2011) & (Movies.release_year < 2015)]
print(Movies_12_14.head(0))
# Movies_12_14.profit = Movies_12_14.revenue - Movies_12_14.budget
# Movies_12_14["profit"] = Movies_12_14.revenue - Movies_12_14.budget
Movies_12_14.loc[:, 'profit'] = Movies_12_14.revenue - Movies_12_14.budget
print(Movies_12_14[Movies_12_14.profit == Movies_12_14.profit.min()].original_title)

# Вопрос 11. Какого жанра фильмов больше всего?
print(Movies.genres.value_counts())
# print(Movies.genres.value_counts().index[0])
# print(Movies.genres.value_counts().values[0])

# Вопрос 12. Какого жанра среди прибыльных фильмов больше всего?
print(Movies[Movies.revenue - Movies.budget > 0].genres.value_counts())

# Вопрос 13. У какого режиссёра самые большие суммарные кассовые сборы?
grouped_director = Movies.groupby(['director'])['revenue'].sum().sort_values(ascending=False)
print(grouped_director.head(10))

# Вопрос 14. Какой режиссер снял больше всего фильмов в стиле Action?
# print(Movies[Movies.genres == 'Action'].director.value_counts())                #  .index[0]
# grouped_director = Movies.groupby(['genres'])['director'].sum().sort_values(ascending=False)
# print(grouped_director.head(10))
