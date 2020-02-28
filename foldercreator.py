import os
import pyfiglet

print(pyfiglet.figlet_format('Welcome to our File operation app'))

help_menu = '''
    Welcome to the command Menu: 
    quit - to exit the application 
    help - to print the help menu 
    delete - to delete folder 
    create - to create folder 
'''

print(help_menu)

# main function
def FolderCreator():
    UserAction = input("Enter your command: ").lower()
    if UserAction == 'help':
        print(help_menu)
        UserAction = input("> ")
    elif UserAction == 'quit':
        print("Thanks for passing by")
        exit(0)

    elif UserAction == 'create':
        try:
            folder_name = input("Enter your folder name: ")
            os.mkdir(folder_name)
            print("Folder created successfully ")
        except FileExistsError:
            print("File already exist")

    elif UserAction == 'delete':
        try:
            folder_name = input("Enter the name of the folder you want delete: ")
            user_prompt = input("Are you sure? 'yes' or 'no' ").lower()
            if user_prompt == 'yes':
                os.rmdir(folder_name)
                print("Folder deleted successfully")
            else:
                print("Exiting, we did not delete the folder")

        except FileNotFoundError:
            print("The Folder you trying to delete does not exist")
    else:
        print("invalid command")

FolderCreator()