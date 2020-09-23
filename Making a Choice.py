def ConvertListToLowerCase(Movies):
    """ Function to convert the list items into lowercase 
    Movies - List of movies to be converted to lowercase """
  
    MoviesList =[]
    for movie in Movies:
        MoviesList.append(movie.lower())
    return MoviesList



if __name__ == "__main__":

    thriller=["Dark","Mindhunter","Parasite","Inception","Insidious","Interstellar","Prison Break","Money Heist","War","Jack Ryan"]
    comedy=["Friends","3 Idiots","Brooklyn 99","How I Met Your Mother","Rick And Morty","The Big Bang Theory","The Office","Space Force"]

    Thriller = ConvertListToLowerCase(thriller)   #Convert thriller list to lowercase
    Comedy = ConvertListToLowerCase(comedy)   #Convert conedy list to lowercase

    Movie = input()   #Take the input Movie/Series

    if Movie.lower() in Thriller:   #Check if the Movie/Series is Thriller
        print("It is a thriller ")
    elif Movie.lower() in Comedy:   #Check if the Movie/Series is Comedy
        print("It is a comedy ")
    else:                          
        print("It's neither comedy nor thriller ")