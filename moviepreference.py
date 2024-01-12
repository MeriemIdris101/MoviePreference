def find_most_preferred_movie_genre(preferences):

    number_of_movie = {}
    # Initilizes counts to 0 for the unseen genres

    max_number_of_movie = 0
    # Initilizes max count to 0


    for preference in preferences:
    # loops each preference
        movie = preference.strip()
        # removes empty whitespaces

        if movie in number_of_movie:
        #checks if movie genre is in dictionary
            number_of_movie[movie] += 1
            #Yes? Then increment count

        else:
            number_of_movie[movie] = 1
            #No? Then add new entry with count 1

        if number_of_movie[movie] > max_number_of_movie:
            max_number_of_movie = number_of_movie[movie]
            # Updates maximum count if current genre has higher count
   
    most_preferred_movie_genre = [movie for movie, count in number_of_movie.items() if count == max_number_of_movie]
    # Uses list to find most preferred movie genre
    return most_preferred_movie_genre


list_of_preference = ['Action', 'Drama', 'Horror', 'Action', 'Thriller', 'Comedy', 'Horror', 'Romance', 'Fantasy', 'Action', 'Documentary']
#Movie preferences (I persoanlly like Thriller the most)

result = find_most_preferred_movie_genre(list_of_preference)
print("Most preferred Movie Genre is:")
for genre in result:
    print(genre)
#Finds and prints most preferred genre
