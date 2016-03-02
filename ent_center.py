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
pans_labyrinth = media.Movie("Pans Labyrinth",
        "Ofelia meets several strange and magical creatures who become central to her story, leading her through the trials of the old labyrinth garden. The",
        "https://upload.wikimedia.org/wikipedia/en/6/67/Pan%27s_Labyrinth.jpg",
        "https://www.youtube.com/watch?v=EqYiSlkvRuw")
# Append movie to list named 'movies'
movies.append(pans_labyrinth)

# Create movie objects and fill in class details
ant_man = media.Movie("Ant-Man",
		"The miniature hero must use his new skills to prevent Cross, also known as Yellowjacket, from perfecting the same technology and using it as a weapon for evil.",
		"https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg",
		"https://www.youtube.com/watch?v=pWdKf3MneyI")
# Append movie to list named 'movies'
movies.append(ant_man)

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
animalhouse = media.Movie("Animal House",
        "The trouble is, the college dean has it in for the Deltas. He has put them on 'Double Secret Probation' and secretly assigned Omega's president the task of having their charter revoked.",
        "https://upload.wikimedia.org/wikipedia/en/e/ea/Animalhouseposter.jpg",
        "https://www.youtube.com/watch?v=HxoBJmyAS04")
# Append movie to list named 'movies'
movies.append(animalhouse)

# use the fresh_tomatoes class to open the html page passing in the movies list as parameters
fresh_tomatoes.open_movies_page(movies)
