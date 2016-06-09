#!/usr/bin/python
# -​*- coding: utf-8 -*​-
# coding=utf8


class Movie():
"""A simple Class based on common movie data
This class provides the following attributes:
	title (str) - original movie title
	overview (str) - basic plot overview
	duration (str) - runtime in minutes
	poser_image_url (str) - url to database location
	trailer_youtube_url (str) - url to YouTube trailer
	rating (str) - either US rating or N/A if no data
"""
	# Class Variables
	VALID_RATINGS = ['N/A', 'G', 'PG', 'PG-13', 'R']

	def __init__(self, info_dict):
		
		self.title				=info_dict['title']
		self.overview			=info_dict['overview']
		self.duration			=info_dict['duration']
		self.poster_image_url	=info_dict['poster']
		self.trailer_youtube_url=info_dict['trailer']
		# If the movie_rating is in the list of valid ratings
		if info_dict['rating'] in self.VALID_RATINGS:
			self.rating	= info_dict['rating']
		else:
			self.rating = 'N/A'