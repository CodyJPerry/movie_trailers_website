#import module
import webbrowser

class Movie():
    """ Creates space in memory when invoked """
    def __init__(self, movie_title, movie_story, movie_image, movie_url):
        """ Arguments to be passed into function for all except self"""
        self.title = movie_title
        self.story = movie_story
        self.box_art = movie_image
        self.youtube_url = movie_url

    def display_trailer(self):
        webbrowser.open(self.youtube_url)
        





        
        
