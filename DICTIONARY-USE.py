import json
from difflib import get_close_matches

def load_dictionary():
    # Load JSON data into a Python dictionary
    with open("data.json") as file:
        data = json.load(file)
    return data

def find_definition(word, data):
    word = word.lower()  # Convert the word to lowercase for case-insensitive search
    if word in data:
        return data[word]
    else:
        # If the word is not found, try to find a close match using difflib
        close_matches = get_close_matches(word, data.keys(), n=1, cutoff=0.8)
        if close_matches:
            suggestion = close_matches[0]
            response = input(f"Did you mean '{suggestion}' instead? Enter 'Y' for Yes, 'N' for No: ")
            if response.lower() == 'y':
                return data[suggestion]
            elif response.lower() == 'n':
                return "Word not found. Please try again."
            else:
                return "Invalid input. Please enter 'Y' or 'N'."
        else:
            return "Word not found. Please try again."

def main():
    dictionary_data = load_dictionary()

    while True:
        user_input = input("Enter a word to search for its definition (type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        else:
            definition = find_definition(user_input, dictionary_data)
            print(definition)

if __name__ == "__main__":
    main()
