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
import random

DATA_FILE = "data.txt"

# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt: str) -> str:
    while True:
        value = input(prompt)
        if value.strip():
            return value
        print("Please enter something (not just spaces).")


# This function repeatedly prompts for input until an integer between 1 and max_value is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_int(prompt: str, max_value: int) -> int:
    while True:
        raw = input(prompt)
        try:
            num = int(raw)
            if 1 <= num <= max_value:
                return num
            print(f"Enter a number between 1 and {max_value}.")
        except ValueError:
            print("Please enter a whole number.")



# This function opens "data.txt" in write mode and writes the data to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data: list) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)



# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.
try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
except Exception as e:
    print(f"[Info] Unable to load existing data: {e}")
    data = []



# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the "One Must Go" Admin Program.')

while True:
    print()
    print("Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.")
    raw_choice = input("> ").strip()

    # Allow quick forms: "s term", "v 2", "d 3"
    parts = raw_choice.split(maxsplit=1)
    choice = parts[0].lower() if parts else ""

        
    if choice == 'a':
        # Add a new category.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
        while True:
            name = input_something("Enter category name: ").strip()
            if any(c["name"].lower() == name.lower() for c in data):
                print("A category with that name already exists. Try another.")
            else:
                break

        # Options: 2–5 unique names; allow 'x' to finish after at least 2
        options = []
        count = 1
        while True:
            upto = f"Enter option {count} "
            tail = '("x" to end): ' if count >= 3 else "(need at least 2): "
            opt = input_something(upto + tail).strip()
            if opt.lower() == "x" and len(options) >= 2:
                break
            if any(o["name"].lower() == opt.lower() for o in options):
                print("That option is already in this category. Use a different name.")
                continue
            options.append({"name": opt, "votes": 0})
            count += 1
            if len(options) == 5:
                print("Maximum of 5 options reached.")
                break

        new_cat = {"name": name, "options": options}
        data.append(new_cat)
        save_data(data)
        print(f'Category added: "{name}" with {len(options)} option(s).')



    
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
