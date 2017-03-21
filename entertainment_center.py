import fresh_tomatoes
import media

# create instances of the Movie class using my favorite movies
deadpool = media.Movie("Deadpool",
                        "A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge.",
                        "http://t1.gstatic.com/images?q=tbn:ANd9GcR-fLY3Z9Vn28UB-A3X_w0vjmkHcXG89HWwul5w6-sg3IonPXA_",
                        "https://youtu.be/ZIM1HydF9UA")

bernies = media.Movie("Weekend at Bernie's",
                     "Two losers try to pretend that their murdered employer is really alive, leading the hitman to attempt to track him down to finish him off.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAwMjU1MTA4N15BMl5BanBnXkFtZTcwNzAxNTc3NA@@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                     "https://youtu.be/YCTgcZ6ImsQ")

other_guys = media.Movie("The Other Guys",
                         "Two mismatched New York City detectives seize an opportunity to step up like the city's top cops whom they idolize -- only things don't quite go as planned.",
                         "http://www.gstatic.com/tv/thumb/movieposters/8045197/p8045197_p_v8_aa.jpg",
                         "https://youtu.be/D6WOoUG1eNo")

# store instances of the Movie class in a list
movies = [deadpool, bernies, other_guys]

# run the open_movies_page function on movies list
fresh_tomatoes.open_movies_page(movies)

