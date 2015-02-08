# movie-site
This is a demonstration of how one can use python with classes, html and css to create a nice little movie page.
There are three main files in this project. 

1. Ent_center
Because we created the class structure in media, this page is very nicely layed out by creating an instance of movie for each title. Each movie instance is added to the movies list which is then passed into 'fresh_tomatoes.py' as a parameter. 

2. Fresh_tomatoes.py
Fresh_tomatoes is the main outline of the site. 
This contains all the JQuery, HTML and CSS that makes this page work.

3. media.py
Media.py shows the basic class creation. Here we include a movie title, movie storyline, poster image and youtube trailer.
 We also add a method called show_trailer that calls the package webbrowser and shows the trailer in a modal.
