import media
import fresh_tomatoes


# Creating movies to describe the instances of the Class Movie


toy_story = media.Movie(
    "Toy Story",
    "A Story of a boy and his toys that come to life",
    "https://orig00.deviantart.net/e2ad/f/2010/071/6/0/toy_story_3_poster_by_jihef03.jpg",  # noqa
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://pre00.deviantart.net/51e1/th/pre/f/2010/192/b/e/avatar_special_edition_poster_by_j_k_k_s.jpg",  # noqa
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie(
    "School of Rock",
    "A teacher forms a band with his students",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

searching_for_sugarman = media.Movie(
    "Searching For Sugarman",
    "Academy Award winning documentary about a 1960's folk icon",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMWYyMzgxNDQtMDI2Mi00NmMzLWI5MTAtMmUwNDg3Yjg3N2U3XkEyXkFqcGdeQXVyNzI1NzMxNzM@._V1_UY268_CR7,0,182,268_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=QL5TffdOQ7g")

all_the_presidents_men = media.Movie(
    "All the President's Men",
    """Two reporters from the Washington Post uncover
    illegal activity at the highest levels of government""",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BOWI2YWQxM2MtY2U4Yi00YjgzLTgwNzktN2ExNTgzNTIzMmUzXkEyXkFqcGdeQXVyMTAwMzUyOTc@._V1_UY1200_CR83,0,630,1200_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=vLt6djxhNe8")

moneyball = media.Movie(
    "Moneyball",
    "An unconventional general manager transforms the Oakland A's",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxOTU3Mzc1M15BMl5BanBnXkFtZTcwMzk1ODUzNg@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=AiAHlZVgXjk")

# Movies array, contains the list of movies as input, which
# is passed to the function "open_movies_page". This function
# translates this list into a web page when we run the
# "entertainment_center.py" file.


movies = [toy_story,
          avatar,
          school_of_rock,
          searching_for_sugarman,
          all_the_presidents_men, 
          moneyball]

fresh_tomatoes.open_movies_page(movies)
