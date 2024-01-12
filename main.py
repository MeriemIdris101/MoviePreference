def find_most_preferred_movie_genre(preferences):

    number_of_movie = {}
    #Initilizes counts to 0 for the unseen genres

    max_number_of_movie = 0
    #Initilizes max count to 0

    most_preferred_movie_by_person = {}
    #Stores most preferred genre for each person, basically a dictionary.

    for person, list_of_genre in preferences.items():
        number_of_movie = {}
        max_number_of_movie = 0
        #Goes through each person and their genre

        for genre in list_of_genre:
            if genre in number_of_movie:
                number_of_movie[genre] += 1
                #Updates count for genres

            else:
                number_of_movie[genre] = 1

            if number_of_movie[genre] > max_number_of_movie:
                max_number_of_movie = number_of_movie[genre]
                #Updates max count if current genre has higher count

        most_preferred_movie_by_person[person] = [genre for genre, count in number_of_movie.items() if count == max_number_of_movie]
        #Finds most preferred genre for current person

    return most_preferred_movie_by_person


preferences = {
    'MichaelBJordan': ['Action', 'Horror', 'Romance', 'Drama', 'Thriller'],
    'Hades': ['Romance', 'Drama', 'Action', 'Thriller', 'Horror'],
    'Posideon': ['Horror', 'Thriller', 'Drama', 'Romance', 'Action'],
    'Lula': ['Drama', 'Romance', 'Action', 'Thriller', 'Horror'],
    'Meriem': ['Thriller', 'Horror', 'Action', 'Drama', 'Romance']
}
#Movie preferences

result = find_most_preferred_movie_genre(preferences)

for person, genres in result.items():
    print(f"{person} prefers {genres[0]} movies.")
#Prints result for every person
