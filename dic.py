import json, pyfiglet

print(pyfiglet.figlet_format('English Dictionary '))

def Dictionary(user_input):
    #open file
    open_dict = json.load(open('Dictionary/data.json'))

    # split the user input into a list
    user_input_split = user_input.split()

    # loop through the words the user type
    for word in user_input_split:
        if word in open_dict:
            print(word, ' - ', open_dict[word][0])
        else:
            print("That word don't exist in our dictionary")

# asking the user for the word
user_input = input("Enter a word to search: ")

# calling the function
Dictionary(user_input)