"""
Code Challenge 13 - Highest Rated Movie Directors

https://pybit.es/codechallenge13.html

* Parse the movie_metadata.csv, using csv.DictReader you get a bunch of
OrderedDicts from which you only need the following k,v pairs:

OrderedDict([...
            ('director_name', 'Lawrence Kasdan'),   
            ...
            ('movie_title', 'Mumford\xa0'),
            ...
            ('title_year', '1999'),
            ...
            ('imdb_score', '6.9'),
            ...

* Only consider directors with a minimum of 4 movies, otherwise you get
misrepresentative data. However going to min 5 movies we miss Sergio
Leone :(

* Take movies of year >= 1960.

* Print the top 20 highest rated directors with their movies ordered
desc on rating.
"""

import csv
from collections import Counter, defaultdict, namedtuple
from urllib import request

MOVIE_DATA = 'https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv'
MOVIES_CSV = 'movies.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

request.urlretrieve(MOVIE_DATA, MOVIES_CSV)

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data=MOVIES_CSV):
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)

    with open(data) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    director_score = []
    count = Counter()

    for director, movies in directors.items(): 
        count[director] += len(movies) 

    # let's get only the five directors with most movies.
    most_movies, _ = zip(*count.most_common(MIN_MOVIES)) 

    for director in most_movies:
        mean_score = _calc_mean(directors[director])
        director_score.append((director, mean_score))

    return director_score


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    total_movies = len(movies)
    sum_score = 0

    for movie in movies:
        sum_score += movie.score

    return sum_score/total_movies


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
