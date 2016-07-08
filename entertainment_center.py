import media
import fresh_tomatoes 

''' list of movies to be loaded'''

avatar = media.Movie("Avatar (2009)", "Enter the World", 
				"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
				"https://www.youtube.com/watch?v=5PSNL1qE6VY")
titanic = media.Movie("Titanic (1997)", "Collide With Destiny", 
				"https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
				"https://www.youtube.com/watch?v=zCy5WQ9S4c0")
star_wars = media.Movie("Star Wars: The Force Awakens (2015)", "A long time ago in a galaxy far, far away...",
			"https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
			"https://www.youtube.com/watch?v=gAUxw4umkdY")

movies = [avatar, titanic, star_wars]

fresh_tomatoes.open_movies_page(movies)
