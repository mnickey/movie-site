__author__ = 'MNickey'
""" Movie Class """

import webbrowser

class Movie():
	"""Movie class construction"""
	def __init__(self, movie_title, movie_storyline,
				poster_image, trailer_youtube):
		self.movie_title = movie_title
		self.movie_storyline = movie_storyline
		self.poster_image = poster_image
		self.trailer_youtube = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube)
