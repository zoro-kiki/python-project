#ZAARA231P023
def add_movie(filename):
    movie_name = input("Enter the movie name to add: ")
    with open(filename, "a") as file:
        file.write(movie_name + "\n")
    print(f"Movie '{movie_name}' added successfully.")
def delete_movie(filename):
    movie_name = input("Enter the movie name to delete: ")
    
    try:
        with open(filename, "r") as file:
            movies = file.readlines()
        movie_exists = False
        with open(filename, "w") as file:
            for movie in movies:
                if movie.strip() != movie_name:
                    file.write(movie)
                else:
                    movie_exists = True
        
        if movie_exists:
            print(f"Movie '{movie_name}' deleted successfully.")
        else:
            print(f"Movie '{movie_name}' not found in the list.")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
def display_movies(filename):
    try:
        with open(filename, "r") as file:
            movies = file.readlines()
        
        if movies:
            print("\nMovies in the list:")
            for movie in movies:
                print(movie.strip())
        else:
            print("No movies in the list.")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
def menu():
    filename = "movies.txt"
    
    while True:
        print("\nMovie Management System by Zaara 231P023")
        print("1. Add Movie")
        print("2. Delete Movie")
        print("3. Display Movies")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_movie(filename)
        elif choice == "2":
            delete_movie(filename)
        elif choice == "3":
            display_movies(filename)
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
if __name__ == "__main__":
    menu()
