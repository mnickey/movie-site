__author__ = 'Michael Nickey'
# Import needed files and classes
import media
import fresh_tomatoes

# Create an empty list to append each movie after creation.
movies = []
# Create movie objects and fill in class details
hackers = media.Movie("Zombie Ass: Toilet of the Dead",
        "A young boy is arrested by the US Secret Service for writing a computer virus and is banned from using a computer until his 18th birthday. Years later, he and his new-found friends discover a plot to unleash a dangerous computer virus, but they must use their computer skills to find the evidence while being pursued by the Secret Service and the evil computer genius behind the virus.",
        "https://upload.wikimedia.org/wikipedia/en/6/67/Hackersposter.jpg",
        "https://www.youtube.com/watch?v=Ql1uLyuWra8")
# Append movie to list named 'movies'
movies.append(hackers)

# Create movie objects and fill in class details
robo_geisha = media.Movie("RoboGeisha",
        "Android geishas battle each other and assassinate targets.",
        "http://upload.wikimedia.org/wikipedia/en/9/96/Robo_geisha.jpg",
        "https://www.youtube.com/watch?v=zgrKLjoWcbs")
# Append movie to list named 'movies'
movies.append(robo_geisha)

# Create movie objects and fill in class details
mutantgs = media.Movie("Mutant Girl Squad",
		"Three super-powered young women battle enemies.",
		"http://upload.wikimedia.org/wikipedia/en/3/39/Mutant-girls-squad-poster.jpg",
		"https://www.youtube.com/watch?v=_SKWQm2sGsg")
# Append movie to list named 'movies'
movies.append(mutantgs)

# Create movie objects and fill in class details
warriors = media.Movie("The Warriors",
		"These are the armies of the night.",
		"http://upload.wikimedia.org/wikipedia/en/0/03/TheWarriors_1979_Movie_Poster.jpg",
		"https://www.youtube.com/watch?v=MV4cgs-bPic")
# Append movie to list named 'movies'
movies.append(warriors)

# Create movie objects and fill in class details
splane = media.Movie("Soul Plane",
        "Determined to create a better flying experience, Nashawn starts his own airline.",
        "http://upload.wikimedia.org/wikipedia/en/0/03/Soul_Plane_poster.jpg",
        "https://www.youtube.com/watch?v=Cf-SXMZTg8I")
# Append movie to list named 'movies'
movies.append(splane)

# Create movie objects and fill in class details
feardotcom = media.Movie("Fear dot com",
        "To catch a killer he must become the victim.",
        "http://upload.wikimedia.org/wikipedia/en/a/a9/FeardotCom_poster.jpg",
        "https://www.youtube.com/watch?v=kSDNIYw1nLI")
# Append movie to list named 'movies'
movies.append(feardotcom)

# use the fresh_tomatoes class to open the html page passing in the movies list as parameters
fresh_tomatoes.open_movies_page(movies)
