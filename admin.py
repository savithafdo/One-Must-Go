# Name: Savitha Fernando
# Student Number: 10705112

# This file is provided to you as a starting point for the "admin.py" program of the Project
# of Programming Principles in Semester 2, 2025.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis of your work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the necessary module(s).
import json



# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):
    pass



# This function repeatedly prompts for input until an integer between 1 and max_value is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_int(prompt, max_value):
    pass



# This function opens "data.txt" in write mode and writes the data to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data):
    pass




# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.




# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the "One Must Go" Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower()
        
    if choice == 'a':
        # Add a new category.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
        pass


    
    elif choice == 'l':
        # List the current categories.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        pass



    elif choice == 's':
        # Search the current categories.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        pass



    elif choice == 'v':
        # View a category.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        pass



    elif choice == 'd':
        # Delete a category.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        pass



    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        pass



    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        pass
