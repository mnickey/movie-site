__author__ = 'MNickey'

import media
import fresh_tomatoes

movies = []

zombie_ass = media.Movie("Zombie Ass: Toilet of the Dead",
        "Megumi and her friends go on a trip to the woods and they are attacked by a crowd undead covered in sewage.",
        "http://upload.wikimedia.org/wikipedia/en/f/f8/Zombie-ass-poster.jpg",
        "https://www.youtube.com/watch?v=XNzduf6vWcA")
movies.append(zombie_ass)

robo_geisha = media.Movie("RoboGeisha",
        "Android geishas battle each other and assassinate targets.",
        "http://upload.wikimedia.org/wikipedia/en/9/96/Robo_geisha.jpg",
        "https://www.youtube.com/watch?v=zgrKLjoWcbs")
movies.append(robo_geisha)

mutantgs = media.Movie("Mutant Girl Squad",
		"Three super-powered young women battle enemies.",
		"http://upload.wikimedia.org/wikipedia/en/3/39/Mutant-girls-squad-poster.jpg",
		"https://www.youtube.com/watch?v=_SKWQm2sGsg")
movies.append(mutantgs)

warriors = media.Movie("The Warriors",
		"These are the armies of the night.",
		"http://upload.wikimedia.org/wikipedia/en/0/03/TheWarriors_1979_Movie_Poster.jpg",
		"https://www.youtube.com/watch?v=MV4cgs-bPic")
movies.append(warriors)

splane = media.Movie("Soul Plane",
        "Determined to create a better flying experience, Nashawn starts his own airline.",
        "http://upload.wikimedia.org/wikipedia/en/0/03/Soul_Plane_poster.jpg",
        "https://www.youtube.com/watch?v=Cf-SXMZTg8I")
movies.append(splane)

feardotcom = media.Movie("Fear dot com",
        "To catch a killer he must become the victim.",
        "http://upload.wikimedia.org/wikipedia/en/a/a9/FeardotCom_poster.jpg",
        "https://www.youtube.com/watch?v=kSDNIYw1nLI")
movies.append(feardotcom)

fresh_tomatoes.open_movies_page(movies)
