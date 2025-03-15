class IncorrectNumberError(Exception):
    pass

# Function to prompt user input until the correct number is entered
def get_correct_number(stored_number):
    while True:
        try:
            # Ask the user to input a number
            user_input = int(input("Enter the correct number: "))
            
            # If the input is incorrect, raise the custom exception
            if user_input != stored_number:
                raise IncorrectNumberError("The entered number is incorrect. Try again.")
            
            # If correct number is entered
            print("Congratulations! You entered the correct number.")
            break  # Exit the loop if the correct number is entered
        
        except IncorrectNumberError as e:
            # Handle the custom exception and print the error message
            print(e)
        except ValueError:
            # Handle case where input is not an integer
            print("Invalid input! Please enter a valid integer.")

# Main program
if __name__ == "__main__":
    stored_number = 42  # The correct number
    get_correct_number(stored_number)

