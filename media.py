import webbrowser


class Movie():
    """ This class provides a way to store movie related information

    Attributes:
        title (str): The movie title
        storyline (str): This contains a short sentence about the movies plot
        poster_image_url (str): The url of the movie poster image
        trailer_youtube_url (str): The url of the movie trailer on youtube
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
