import sys

def count_file_content(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            
            num_lines = len(lines)
            num_words = 0
            num_chars = 0

            for line in lines:
                words = line.split()  # Split the line into words
                num_words += len(words)  # Count words
                num_chars += len(line)  # Count characters (including spaces and newlines)
            print("Zaara 231P023")
            print(f"Number of Lines: {num_lines}")
            print(f"Number of Words: {num_words}")
            print(f"Number of Characters: {num_chars}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]  # Command-line argument se filename lena
        count_file_content(file_name)
    else:
        print("Usage: python pyexp4.py <file_name>")
