#import module
import webbrowser

class Movie():
    #creates space in memory
    def __init__(self, movie_title, movie_story, movie_image, movie_url):
        self.title = movie_title
        self.story = movie_story
        self.box_art = movie_image
        self.youtube_url = movie_url

    def display_trailer(self):
        webbrowser.open(self.youtube_url)
        





        
        
