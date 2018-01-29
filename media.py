import webbrowser
#this way you can open up a trailer in a browser

class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    #Init function creates memory space for properties of the class
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Displays movie trailer in a web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
    
