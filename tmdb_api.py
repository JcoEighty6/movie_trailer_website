#!/usr/bin/python
# -​*- coding: utf-8 -*​-
# coding=utf8
import tmdbsimple as tmdb

"""
This module uses "The Movie Database" in order to pull
movie information from their API. The tmdb_api class is 
a wrapper which more effeciently gathers common information.
"""



class tmdb_api():
	'''Custom TMDB API wrapper class
	This class allows simpler access to common movie data through the
	tmdb api.
	
	!!!IMPORTANT!!! - You must set your API key to be able to use this class

	The only input required is a movie ID which can be found by searching
	for a movie using the following link:
		https://api.themoviedb.org/3/search/movie?api_key='###'&query=matrix
		- simply replace the query= value with whatever you need.

	Class Attributes:
		API_KEY (str) - your api key
		movie_id (str) - the id of the movie you wish to access data about
		api_caller (obj) - api connection object used to make api calls
		response (obj) - obj used to store JSON response data
		title (str) - the movie's original title
		overview (str) - the movie's basic plot overview
		poster (str) - returns a full path to movie poster
		rating (str) - the US certification (rating) for the movie
		trailer (str) - returns a full youtube path
		duration (str) - the runtime of the movie in minutes
		common_info (dict) - a dictionary of commonly used data:
							{title, overview, poster, rating
							 trailer, duration}

	'''

	# This is required to build the path for posters and logos
	IMAGE_PATH = 'http://image.tmdb.org/t/p/original'

	# This is required to build the path for YouTube trailers and clips
	YOUTUBE_PATH = 'http://youtube.com/watch?v='

	def __init__(self, movie_id):
		self.API_KEY 	= tmdb.API_KEY = 'de26bf8f90a538024a107e61f2a8b9e3'
		self.movie_id 	= movie_id
		self.api_caller = tmdb.Movies(self.movie_id)
		self.response 	= self.api_caller.info()
		self.title 		= self.api_caller.title
		self.overview 	= self.api_caller.overview
		self.poster 	= IMAGE_PATH + str(self.api_caller.poster_path)
		self.rating 	= self.us_rating(self.api_caller)
		self.trailer 	= YOUTUBE_PATH + self.trailer_key(self.api_caller)
		self.duration	= self.api_caller.runtime
		self.common_info= {'title':		self.title,
						   'overview':	self.overview,
						   'poster':	self.poster,
						   'rating':	self.rating,
						   'trailer':	self.trailer,
						   'duration':	self.duration}

	# Pull the YouTube movie key from the API and return it as a string
	def trailer_key(self, api_caller):
		return str(api_caller.videos()['results'].pop()['key'])

	# Pull the US rating cert. from the API and return it or N/A
	def us_rating(self, api_caller):
		for item in api_caller.releases()['countries']:
			if item['iso_3166_1'] == 'US':
				flag   = True
				rating = str(item['certification'])

		if flag:
			return rating
		else:
			return 'N/A'