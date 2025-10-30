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

# This is where we store all our game data like categories and votes
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
    # Keep asking until we get a valid number
    while True:
        # Get user input as text
        raw = input(prompt)
        try:
            # Try to convert the text to a number
            num = int(raw)
            # Check if the number is in the valid range
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
        # Keep track of all options entered
        options = []
        # Start counting from option 1
        count = 1
        while True:
            # Build the prompt showing which option number we're on
            upto = f"Enter option {count} "
            # After 2 options, user can type 'x' to finish
            tail = '("x" to end): ' if count >= 3 else "(need at least 2): "
            opt = input_something(upto + tail).strip()
            # Let user finish if they typed 'x' and we have enough options
            if opt.lower() == "x" and len(options) >= 2:
                break
            # Make sure this option name isn't already used
            if any(o["name"].lower() == opt.lower() for o in options):
                print("That option is already in this category. Use a different name.")
                continue
            # Add the new option (starting with 0 votes)
            options.append({"name": opt, "votes": 0})
            count += 1
            # Don't allow more than 5 options
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
        if not data:
            print("No categories saved.")
        else:
            print("List of categories:")
            for i, cat in enumerate(data, start=1):
                total_votes = sum(o["votes"] for o in cat.get("options", []))
                print(f'{i}) {cat["name"]} ({len(cat["options"])} options, {total_votes} votes)')




    elif choice == 's':
        # Search the current categories.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print("No categories saved.")
            continue
        # Get search term from command (like 's food') or ask user to type it
        term = parts[1] if len(parts) == 2 and parts[1].strip() else input_something("Enter search term: ")
        # Convert to lowercase so searching isn't case sensitive
        t = term.lower()
        # Keep track of what we find
        results = []
        for idx, cat in enumerate(data, start=1):
            # Check if search term appears in the category name
            name_hit = t in cat["name"].lower()
            # Check if search term appears in any of the options
            options_hit = any(t in opt["name"].lower() for opt in cat["options"])
            # If we found a match, save the category's info
            if name_hit or options_hit:
                total_votes = sum(o["votes"] for o in cat["options"])
                results.append((idx, cat["name"], len(cat["options"]), total_votes))
        if not results:
            print("No results found.")
        else:
            print("Search results:")
            for idx, name, nopts, tvotes in results:
                print(f"{idx}) {name} ({nopts} options, {tvotes} votes)")




    elif choice == 'v':
        # View a category.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print("No categories saved.")
            continue
        if len(parts) == 2 and parts[1].isdigit():
            index_one_based = int(parts[1])
        else:
            index_one_based = input_int("Enter category number to view: ", len(data))
        i = index_one_based - 1
        cat = data[i]
        print()
        print(cat["name"])
        if all(o["votes"] == 0 for o in cat["options"]):
            print("No votes recorded")
        else:
            # Show options ordered by votes (display only; do not mutate stored order)
            ordered = sorted(cat["options"], key=lambda o: o["votes"], reverse=True)
            total = sum(o["votes"] for o in ordered) or 1
            for opt in ordered:
                pct = f' ({round(opt["votes"] * 100 / total)}%)' if total else ""
                print(f'  - {opt["name"]}: {opt["votes"]} vote(s){pct}')




    elif choice == 'd':
        # Delete a category.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print("No categories saved.")
            continue
        if len(parts) == 2 and parts[1].isdigit():
            index_one_based = int(parts[1])
        else:
            index_one_based = input_int("Enter category number to delete: ", len(data))
        i = index_one_based - 1
        removed = data.pop(i)
        save_data(data)
        print(f'Category deleted: "{removed["name"]}".')



    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        print('Goodbye! Thank you for using the "One Must Go" admin program.')
        break



    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        print("Invalid choice.")
