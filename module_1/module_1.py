import pandas as pd

Movies = pd.read_csv('c:/Users/Дмитрий/PycharmProjects/movie_bd_v5.csv')
# Movies = pd.read_csv('movie_bd_v5.csv')

# Вопрос 1. У какого фильма из списка самый большой бюджет?
print('Вопрос 1. У какого фильма из списка самый большой бюджет?')
print(Movies[Movies.budget == Movies.budget.max()].original_title)
print()

# Вопрос 2. Какой из фильмов самый длительный (в минутах)?
print('Вопрос 2. Какой из фильмов самый длительный (в минутах)?')
print(Movies[Movies.runtime == Movies.runtime.max()].original_title)
print()

# Вопрос 3. Какой из фильмов самый короткий (в минутах)?
print('Вопрос 3. Какой из фильмов самый короткий (в минутах)?')
print(Movies[Movies.runtime == Movies.runtime.min()].original_title)
print()

# Вопрос 4. Какова средняя длительность фильмов?
print('Вопрос 4. Какова средняя длительность фильмов?')
print(Movies.runtime.mean())
print()

# Вопрос 5. Каково медианное значение длительности фильмов?
print('Вопрос 5. Каково медианное значение длительности фильмов?')
print(Movies.runtime.describe())
print()

# Вопрос 6. Какой фильм самый прибыльный?
print('Вопрос 6. Какой фильм самый прибыльный?')
Movies.profit = Movies.revenue - Movies.budget
Movies["profit"] = Movies.revenue - Movies.budget
print(Movies[Movies.profit == Movies.profit.max()].original_title)
print()

# Вопрос 7. Какой фильм самый убыточный?
print('Вопрос 7. Какой фильм самый убыточный?')
print(Movies[Movies.profit == Movies.profit.min()].original_title)
print()

# Вопрос 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?
print('Вопрос 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?')
print(Movies[Movies.revenue - Movies.budget > 0].value_counts())
print()

# Вопрос 9. Какой фильм оказался самым кассовым в 2008 году?
print('Вопрос 9. Какой фильм оказался самым кассовым в 2008 году?')
Movies_2008 = Movies[Movies.release_year == 2008]
print(Movies_2008[Movies_2008.revenue == Movies_2008.revenue.max()].original_title)
print()

# Вопрос 10. Самый убыточный фильм за период с 2012 по 2014 годы (включительно)?
print('Вопрос 10. Самый убыточный фильм за период с 2012 по 2014 годы (включительно)?')
Movies_12_14 = Movies[(Movies.release_year > 2011) & (Movies.release_year < 2015)]
# print(Movies_12_14.head(0))
# Movies_12_14.profit = Movies_12_14.revenue - Movies_12_14.budget
Movies_12_14["profit"] = Movies_12_14.revenue - Movies_12_14.budget
Movies_12_14.loc[:, 'profit'] = Movies_12_14.revenue - Movies_12_14.budget
print(Movies_12_14[Movies_12_14.profit == Movies_12_14.profit.min()].original_title)
print()

# Вопрос 11. Какого жанра фильмов больше всего?
# print(Movies.genres.value_counts())
print("Вопрос 11. Какого жанра фильмов больше всего?")
'''
print("Основной жанр")
print("Action", Movies[Movies.genres.str.match("Action", na=False)].imdb_id.count())
print("Adventure", Movies[Movies.genres.str.match("Adventure", na=False)].imdb_id.count())
print("Drama", Movies[Movies.genres.str.match("Drama", na=False)].imdb_id.count())
print("Comedy", Movies[Movies.genres.str.match("Comedy", na=False)].imdb_id.count())
print("Thriller", Movies[Movies.genres.str.match("Thriller", na=False)].imdb_id.count())
'''

# '''
print("Action", Movies[Movies.genres.str.contains("Action", na=False)].imdb_id.count())
print("Adventure", Movies[Movies.genres.str.contains("Adventure", na=False)].imdb_id.count())
print("Drama", Movies[Movies.genres.str.contains("Drama", na=False)].imdb_id.count())
print("Comedy", Movies[Movies.genres.str.contains("Comedy", na=False)].imdb_id.count())
print("Thriller", Movies[Movies.genres.str.contains("Thriller", na=False)].imdb_id.count())
print()
# '''

# print(Movies[Movies.genres.str.contains("Action", na=False)].count())
# print(Movies.genres.value_counts().index[0])
# print(Movies.genres.value_counts().values[0])

# Вопрос 12. Какого жанра среди прибыльных фильмов больше всего?
'''
profit_Movies = Movies[Movies.revenue > Movies.budget].reset_index()
print("Основной жанр")
print("Action", profit_Movies[profit_Movies.genres.str.match("Action", na=False)].imdb_id.count())
print("Adventure", profit_Movies[profit_Movies.genres.str.match("Adventure", na=False)].imdb_id.count())
print("Drama", profit_Movies[profit_Movies.genres.str.match("Drama", na=False)].imdb_id.count())
print("Comedy", profit_Movies[profit_Movies.genres.str.match("Comedy", na=False)].imdb_id.count())
print("Thriller", profit_Movies[profit_Movies.genres.str.match("Thriller", na=False)].imdb_id.count())
'''

# '''
print("Вопрос 12. Какого жанра среди прибыльных фильмов больше всего?")
profit_Movies = Movies[Movies.revenue > Movies.budget].reset_index()
print("Action", profit_Movies[profit_Movies.genres.str.contains("Action", na=False)].imdb_id.count())
print("Adventure", profit_Movies[profit_Movies.genres.str.contains("Adventure", na=False)].imdb_id.count())
print("Drama", profit_Movies[profit_Movies.genres.str.contains("Drama", na=False)].imdb_id.count())
print("Comedy", profit_Movies[profit_Movies.genres.str.contains("Comedy", na=False)].imdb_id.count())
print("Thriller", profit_Movies[profit_Movies.genres.str.contains("Thriller", na=False)].imdb_id.count())
# '''
print()

print('Вопрос 13. У какого режиссёра самые большие суммарные кассовые сборы?')
grouped_director = Movies.groupby(['director'])['revenue'].sum().sort_values(ascending=False)
print(grouped_director.head(5))
print()

# Вопрос 14. Какой режиссер снял больше всего фильмов в стиле Action?
print('Вопрос 14. Какой режиссер снял больше всего фильмов в стиле Action?')
# print(Movies[Movies.genres.str.contains("Action", na=False)].director.value_counts().head(20))
print(Movies[Movies.genres.str.match("Action", na=False)].director.value_counts().head(5))
print()
# grouped_director = Movies.groupby(['genres'])['director'].sum().sort_values(ascending=False)
# print(grouped_director.head(10))

# Вопрос 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году?
Movies_2012 = Movies[Movies.release_year == 2012]
# '''
print("Вопрос 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году?")
print("Nicolas Cage", Movies_2012[Movies_2012.cast.str.contains("Nicolas Cage", na=False)]['revenue'].sum())
print("Tom Hardy", Movies_2012[Movies_2012.cast.str.contains("Tom Hardy", na=False)]['revenue'].sum())
print("Chris Hemsworth", Movies_2012[Movies_2012.cast.str.contains("Chris Hemsworth", na=False)]['revenue'].sum())
print("Jim Sturgess", Movies_2012[Movies_2012.cast.str.contains("Jim Sturgess", na=False)]['revenue'].sum())
print("Emma Stone", Movies_2012[Movies_2012.cast.str.contains("Emma Stone", na=False)]['revenue'].sum())
# '''
print()

# Вопрос 16. Какой актер снялся в большем количестве высокобюджетных фильмов?
# Примечание: в фильмах, где бюджет выше среднего по данной выборке.
high_budget_Movies = Movies[Movies.budget > Movies.budget.mean()]
# '''
print('Вопрос 16. Какой актер снялся в большем количестве высокобюджетных фильмов?')
print("Tom Cruise", high_budget_Movies[high_budget_Movies.cast.str.contains("Tom Cruise", na=False)]['revenue'].count())
print("Mark Wahlberg", high_budget_Movies[high_budget_Movies.cast.str.contains("Mark Wahlberg", na=False)]['revenue'].count())
print("Matt Damon", high_budget_Movies[high_budget_Movies.cast.str.contains("Matt Damon", na=False)]['revenue'].count())
print("Angelina Jolie", high_budget_Movies[high_budget_Movies.cast.str.contains("Angelina Jolie", na=False)]['revenue'].count())
print("Adam Sandler", high_budget_Movies[high_budget_Movies.cast.str.contains("Adam Sandler", na=False)]['revenue'].count())
# '''
print()

# Вопрос 17. В фильмах какого жанра больше всего снимался Nicolas Cage?
Nicolas_Cage = Movies[Movies.cast.str.contains("Nicolas Cage", na=False)]
# '''
print("Вопрос 17. В фильмах какого жанра больше всего снимался Nicolas Cage?")
print("Drama", Nicolas_Cage[Nicolas_Cage.genres.str.contains("Drama", na=False)].imdb_id.count())
print("Action", Nicolas_Cage[Nicolas_Cage.genres.str.contains("Action", na=False)].imdb_id.count())
print("Thriller", Nicolas_Cage[Nicolas_Cage.genres.str.contains("Thriller", na=False)].imdb_id.count())
print("Adventure", Nicolas_Cage[Nicolas_Cage.genres.str.contains("Adventure", na=False)].imdb_id.count())
print("Crime", Nicolas_Cage[Nicolas_Cage.genres.str.contains("Crime", na=False)].imdb_id.count())
# '''
print()

# Вопрос 18. Самый убыточный фильм от Paramount Pictures?
Paramount_Pictures = Movies[Movies.production_companies.str.contains("Paramount Pictures", na=False)].reset_index()
Paramount_Pictures['unprofit'] = Paramount_Pictures['budget'] - Paramount_Pictures['revenue']
print('Вопрос 18. Самый убыточный фильм от Paramount Pictures?')
print("The most unprofitable\n",
      Paramount_Pictures[Paramount_Pictures.unprofit == Paramount_Pictures.unprofit.max()].original_title)
print()

# Вопрос 19. Какой год стал самым успешным по суммарным кассовым сборам?
print("Вопрос 19. Какой год стал самым успешным по суммарным кассовым сборам?")
grouped_revenue = Movies.groupby(['release_year'])['revenue'].sum().sort_values(ascending=False)
print(grouped_revenue.head(5))
print()

# Вопрос 20. Какой самый прибыльный год для студии Warner Bros?
print("Вопрос 20. Какой самый прибыльный год для студии Warner Bros?")
Warner_Bros = Movies[Movies.production_companies.str.contains("Warner Bros", na=False)].reset_index()
grouped_revenue_WB = Warner_Bros.groupby(['release_year'])['revenue'].sum().sort_values(ascending=False)
print(grouped_revenue_WB.head(5))
print()

# Вопрос 21. В каком месяце за все годы суммарно вышло больше всего фильмов?
print("Вопрос 21. В каком месяце за все годы суммарно вышло больше всего фильмов?")
# grouped_revenue_WB = Warner_Bros.groupby(['release_year'])['revenue'].sum().sort_values(ascending=False)
print(Movies[Movies.release_date.str.match("1/", na=False)].imdb_id.count())
print(Movies[Movies.release_date.str.match("5/", na=False)].imdb_id.count())
print(Movies[Movies.release_date.str.match("6/", na=False)].imdb_id.count())
print(Movies[Movies.release_date.str.match("9/", na=False)].imdb_id.count())
print(Movies[Movies.release_date.str.match("12/", na=False)].imdb_id.count())
print()

# Вопрос 22. Сколько суммарно вышло фильмов летом (за июнь, июль, август)?
print("Вопрос 22. Сколько суммарно вышло фильмов летом (за июнь, июль, август)?")
# grouped_revenue_WB = Warner_Bros.groupby(['release_year'])['revenue'].sum().sort_values(ascending=False)
print(sum([ Movies[Movies.release_date.str.match(str(month), na=False)].imdb_id.count() for month in [6, 7, 8] ]))
# print(Movies[Movies.release_date.str.match("6", na=False)].imdb_id.count())
# print(Movies[Movies.release_date.str.match("7", na=False)].imdb_id.count())
# print(Movies[Movies.release_date.str.match("8", na=False)].imdb_id.count())
print()

# Вопрос 23. Какой режиссер выпускает (суммарно по годам) больше всего фильмов зимой?
print("Вопрос 23. Какой режиссер выпускает (суммарно по годам) больше всего фильмов зимой?")
directors = ['Steven Soderbergh', 'Christopher Nolan', 'Clint Eastwood', 'Ridley Scott', 'Peter Jackson']
for director in directors:
    print(director, sum([ Movies[Movies.release_date.str.match((str(month)+'/') or ((str(month)+'.')), na=False)
                  & (Movies.director == director)].imdb_id.count() for month in [1, 2, 12] ]))
'''
print('Steven Soderbergh', sum([ Movies[Movies.release_date.str.match(str(month)+'/', na=False)
                                        & (Movies.director == 'Steven Soderbergh')].imdb_id.count() for month in [1, 2, 12] ]))
print('Christopher Nolan', sum([ Movies[Movies.release_date.str.match(str(month)+'/', na=False)
                                        & (Movies.director == 'Christopher Nolan')].imdb_id.count() for month in [1, 2, 12] ]))
print('Clint Eastwood', sum([ Movies[Movies.release_date.str.match(str(month)+'/', na=False)
                                        & (Movies.director == 'Clint Eastwood')].imdb_id.count() for month in [1, 2, 12] ]))
print('Ridley Scott', sum([ Movies[Movies.release_date.str.match(str(month)+'/', na=False)
                                        & (Movies.director == 'Ridley Scott')].imdb_id.count() for month in [1, 2, 12] ]))
print('Peter Jackson', sum([ Movies[Movies.release_date.str.match(str(month)+'/', na=False)
                                        & (Movies.director == 'Peter Jackson')].imdb_id.count() for month in [1, 2, 12] ]))
'''
print()

# Вопрос 24. Какая студия даёт самые длинные названия своим фильмам по количеству символов?
print("Вопрос 24. Какая студия даёт самые длинные названия своим фильмам по количеству символов?")
studios = ['Universal Pictures', 'Warner Bros', 'Jim Henson Company, The', 'Paramount Pictures', 'Four By Two Productions']
for studio in studios:
    studio_df = Movies[Movies.production_companies.str.contains(studio, na=False)].reset_index()
    print(studio, studio_df.original_title.str.len().mean())
print()

# Вопрос 25. Описания фильмов какой студии в среднем самые длинные по количеству слов?
print("Вопрос 25. Описания фильмов какой студии в среднем самые длинные по количеству слов?")
studios = ['Universal Pictures', 'Warner Bros', 'Midnight Picture Show', 'Paramount Pictures', 'Total Entertainment']
for studio in studios:
    studio_df = Movies[Movies.production_companies.str.contains(studio, na=False)].reset_index()
    print(studio, studio_df.overview.str.len().mean())
print()

# Вопрос 26. Какие фильмы входят в один процент лучших по рейтингу?
print("Вопрос 26. Какие фильмы входят в один процент лучших по рейтингу?")
'''
Movies = [['Inside Out', 'The Dark Knight', '12 Years a Slave'], ['BloodRayne', 'The Adventures of Rocky & Bullwinkle'],
          ['Batman Begins', 'The Lord of the Rings: The Return of the King', 'Upside Down'],
          ['300', 'Lucky Number Slevin', 'Kill Bill: Vol. 1'], ['Upside Down', 'Inside Out', 'Iron Man']]
for Set in Movies:
    print(Set, Movies[Movies.cast.str.contains(pair[0], na=False) &
                       Movies.cast.str.contains(pair[1], na=False)].imdb_id.count())
'''
Movies_100 = Movies['vote_average'].value_counts(bins=100)
print(Movies_100)
print(Movies[Movies['vote_average'] > Movies_100.index[1].left].index.nunique())
print()

# Вопрос 27. Какие актеры чаще всего снимаются в одном фильме вместе?
print("Вопрос 27. Какие актеры чаще всего снимаются в одном фильме вместе?")
actors = [['Johnny Depp', 'Helena Bonham Carter'], ['Ben Stiller', 'Owen Wilson'], ['Vin Diesel', 'Paul Walker'],
          ['Adam Sandler', 'Kevin James'], ['Daniel Radcliffe', 'Rupert Grint']]
for pair in actors:
    print(pair, Movies[Movies.cast.str.contains(pair[0], na=False) &
                       Movies.cast.str.contains(pair[1], na=False)].imdb_id.count())
print()

