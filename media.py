"""
module to display movie object, attributes and instances
"""

import webbrowser


class Movie:
    """This is a doc about movies"""

    VALID_RATINGS = ["G", "PG", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):  # noqa
        """
        This function allows for the creation of a movie object that returns
        key pieces of information about a given movie
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        This function opens a browser window and displays the youtube
        trailer for a given feature
        """
        webbrowser.open(self.trailer_youtube_url)
