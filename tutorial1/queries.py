from actor import Actor
from base import Session
from contact_details import ContactDetails
from movie import Movie
from datetime import date

#extract a session
session = Session()

#extract all movies
movies = session.query(Movie).all()

#4 - print movies details
print('\n### All Movies:')
for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')
    print('')

#get the movies after 15-01-01
movies = session.query(Movie) \
      .filter(Movie.release_date > date(2015, 1, 1)) \
      .all()

print('### Recent movies:')
for movie in movies:
    print(f'{movie.title} was released after 2015')
    print('')

#movies that dwayne johnson participated in
the_rock_movies = session.query(Movie) \
       .join(Actor, Movie.actors) \
       .filter(Actor.name == 'Dwayne Johnson') \
       .all()

print('### Dwayne Johnson Movies:')
for movie in movies:
    print(f'The Rock starred in {movie.title}')
    print('')

#get actors that have a house in glendale
glendale_stars = session.query(Actor) \
       .join(ContactDetails) \
       .filter(ContactDetails.address.ILIKE('%glendale%')) \
       .all()

print('### Actors that live in Glendale:')
for actor in glendale_stars:
    print(f'{actor.name} has a house in Glendale')
    print('')
