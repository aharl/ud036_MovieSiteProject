import media
import fresh_tomatoes


# Create instances of the Movie class for the movies in our list
alien = media.Movie("Alien",
                    "The commercial spacecraft Nostromo is on a return trip to"
                    " Earth with a seven-member crew in stasis",
                    "https://upload.wikimedia.org/wikipedia/en/c/c3/"
                    "Alien_movie_poster.jpg",
                    "https://www.youtube.com/watch?v=NZ3qKyPxCP0")
blade_runner = media.Movie("Blade Runner",
                           "In Los Angeles in November 2019, ex-police officer"
                           " Rick Deckard is detained by officer Gaff and"
                           " brought to his former supervisor, Bryant.",
                           "https://upload.wikimedia.org/wikipedia/en/5/53/"
                           "Blade_Runner_poster.jpg",
                           "https://www.youtube.com/watch?v=73rx9W5Tmzg")
thelma_and_louise = media.Movie("Thelma & Louise",
                                "Two friends, Thelma Dickinson and Louise"
                                " Sawyer, set out for a two-day vacation to"
                                " take a break from their dreary lives in"
                                " Arkansas.",
                                "https://upload.wikimedia.org/wikipedia/en/d/"
                                "de/Thelma_%26_Louiseposter.jpg",
                                "https://www.youtube.com/watch?v=qS8bgqhYoZg")
black_hawk_down = media.Movie("Black Hawk Down",
                              "In 1993, following the ousting of the central"
                              " government and start of a civil war, a major"
                              " United Nations military operation in Somalia"
                              " is authorized with a peacekeeping mandate.",
                              "https://upload.wikimedia.org/wikipedia/en/0/0c/"
                              "Black_hawk_down_ver1.jpg",
                              "https://www.youtube.com/watch?v=_Ygi2lDAdLo")
gladiator = media.Movie("Gladiator",
                        "In AD 180, Hispano-Roman General Maximus Decimus"
                        " Meridius leads the Roman army to a decisive victory"
                        " against the Germanic tribes near Vindobona on the"
                        " northern frontier.",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/"
                        "Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=l-kV68xPVnM")
matchstick_men = media.Movie("Matchstick Men",
                             "Roy Waller is a con artist residing in Los"
                             " Angeles with severe tourette's syndrome and"
                             " obsessive-compulsive disorder.",
                             "https://upload.wikimedia.org/wikipedia/en/8/8e/"
                             "Matchstick_Men.jpg",
                             "https://www.youtube.com/watch?v=kK1x-RlILQI")

# Array of movie objects
movies = [alien,
          blade_runner,
          thelma_and_louise,
          black_hawk_down,
          gladiator,
          matchstick_men]

# Build html page using movie list
fresh_tomatoes.open_movies_page(movies)
