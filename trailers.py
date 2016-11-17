#import modules
import movie
import open_browser

#use class 'Movie' to create instances/objects
harry_potter = movie.Movie("Harry Potter and the Order of the Phoenix",
                           "Harry and Dumbledore are targeted by the Wizard authorities as an authoritarian bureaucrat slowly seizes power at Hogwarts.",
                           "http://www.harrypottermovieposters.com/wp-content/uploads/2013/08/harry-potter-and-the-order-of-the-phoenix-movie-poster-style-h.jpg",
                           "https://www.youtube.com/watch?v=y6ZW7KXaXYk")

doctor_strange = movie.Movie("Doctor Strange",
                             "Dr. Stephen Strange's (Benedict Cumberbatch) life changes after a car accident robs him of the use of his hands.",
                             "http://static.srcdn.com/wp-content/uploads/Doctor-Strange-Poster.jpg",
                             "https://www.youtube.com/watch?v=HSzx-zryEgM")

captain_america = movie.Movie("Captain America Civil War",
                              "Political pressure mounts to install a system of accountability when the actions of the Avengers lead to collateral damage.",
                              "http://www.flickeringmyth.com/wp-content/uploads/2016/03/Civil-War-International-Poster.jpg",
                              "https://www.youtube.com/watch?v=dKrVegVI0Us")

hunger_games = movie.Movie("Hunger Games Catching Fire",
                           "As she and Peeta travel throughout the districts, Katniss senses a rebellion is stirring.",
                           "http://moviefiles.alphacoders.com/179/poster-1792.jpg",
                           "https://www.youtube.com/watch?v=zoKj7TdJk98")

never_back_down = movie.Movie("Never Back Down: No Surrender",
                              "Case Walker (Michael Jai White), a former MMA champion, begins to stage a comeback and make another run at the title, pitting his old school skills against fighters from the new breed.",
                              "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Never_Back_Down_3.jpg/220px-Never_Back_Down_3.jpg",
                              "https://www.youtube.com/watch?v=dlyVshoWJDE")

the_dark_knight = movie.Movie("The Dark Knight",
                             "When a vile young criminal calling himself the Joker (Heath Ledger) suddenly throws the town into chaos, the caped Crusader begins to tread a fine line between heroism and vigilantism.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                             "https://www.youtube.com/watch?v=EXeTwQWrcwY")


#store instances/objects of movies in an list
movie_list = [doctor_strange, captain_america, hunger_games, never_back_down, the_dark_knight, harry_potter]

#invoke function to display movies
open_browser.open_movies_page(movie_list)
