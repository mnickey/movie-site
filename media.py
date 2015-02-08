__author__ = 'Michael Nickey'

# Import the needed requirements
import webbrowser
# Create the class named Movie
class Movie():
	"""Movie class construction"""
    # Start the classes created with some basic structures
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.movie_title = movie_title
		self.movie_storyline = movie_storyline
		self.poster_image = poster_image
		self.trailer_youtube = trailer_youtube

	# Create a method that will allow each class to open a youtube trailer
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube)