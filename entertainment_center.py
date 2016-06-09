#!/usr/bin/python
# -​*- coding: utf-8 -*​-
# coding=utf8
import media
import fresh_tomatoes
from tmdb_api import tmdb_api as api

'''
This is the main info that the favorites website will be populated
with. This module relies on the custom api wrapper called tmdb_api.

The Movie Id's which are used to instantiate the API can be found by
searching for movie titles using the following example url.

https://api.themoviedb.org/3/search/movie?api_key='YOUR_API_KEY'&query=matrix
- simply replace the query= value with whatever you need.

Id's are the value previous to "original_title" in the JSON response
'''

# Set initial api callers for accessing tmdb data
the_matrix_api 			= api(603)
fight_club_api 			= api(550)
boondock_saints_api 	= api(8374)
saving_private_ryan_api = api(857)
toy_soldiers_api		= api(10750)
the_hunted_api			= api(10632)
star_wars_four_api		= api(11)
star_wars_five_api		= api(1891)
star_wars_six_api		= api(1892)

# Instantiate Movie class instances
the_matrix 				= media.Movie(the_matrix_api.common_info)
fight_club 				= media.Movie(fight_club_api.common_info)
boondock_saints 		= media.Movie(boondock_saints_api.common_info)
saving_private_ryan 	= media.Movie(saving_private_ryan_api.common_info)
toy_soldiers			= media.Movie(toy_soldiers_api.common_info)
the_hunted				= media.Movie(the_hunted_api.common_info)
star_wars_four			= media.Movie(star_wars_four_api.common_info)
star_wars_five			= media.Movie(star_wars_five_api.common_info)
star_wars_six			= media.Movie(star_wars_six_api.common_info)

# Create list of movies for Fresh Tomatoes population
movies = [the_matrix, fight_club, boondock_saints, saving_private_ryan, 
		  toy_soldiers, the_hunted, star_wars_four, star_wars_five,
		  star_wars_six]

# Sort movies alphabetically based on Movie.title attribute
movies = sorted(movies, key=lambda movie: movie.title)

# Instatiate and launch website
fresh_tomatoes.open_movies_page(movies)


