# Name: Savitha Fernando
# Student Number: 10705112

# This file is provided to you as a starting point for the "omg.py" program of the Project
# of Programming Principles in Semester 2, 2025.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis of your work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the necessary module(s).
import tkinter, tkinter.messagebox, json
import json
import tkinter as tk
from tkinter import messagebox

DATA_FILE = "data.txt"

class ProgramGUI:

    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading the data from the text file and creating the user interface.
        # See the "Constructor of the GUI Class of omg.py" section of the assignment brief.
        # --- Load data once ---
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except Exception:
            messagebox.showerror("Missing/Invalid file", "Could not open or parse data.txt.")
            return
        if not isinstance(self.data, list) or not self.data:
            messagebox.showerror("No categories", "There are no categories to show.")
            return

        self.root = tk.Tk()
        self.root.title("One Must Go")
        
        self.root.geometry("+95+95")
        self.root.resizable(False, False)

        self.index = 0  # current category

        wrapper = tk.Frame(self.root, padx=16, pady=16)
        wrapper.pack(fill="both", expand=True)

        tk.Label(wrapper, text="The category is...").pack(anchor="w")

        self.lbl_title = tk.Label(wrapper, text="", font=("Impact", 22), fg="#488BCC")
        self.lbl_title.pack(anchor="w", pady=(0, 8))

        tk.Label(wrapper, text="Which one must go?").pack(anchor="w", pady=(0, 8))

        self.options_frame = tk.Frame(wrapper)
        self.options_frame.pack(anchor="w", pady=(0, 8))

        self.lbl_progress = tk.Label(wrapper, text="")
        self.lbl_progress.pack(anchor="w")

        self.show_category()

        self.root.mainloop()



    def show_category(self):
        # This method displays the name and option buttons of the current category in the GUI.
        # See Point 1 of the "Methods in the GUI class of omg.py" section of the assignment brief.
        cat = self.data[self.index]
        self.lbl_title.config(text=cat["name"])

        for child in list(self.options_frame.children.values()):
            child.destroy()

        longest = max((len(o["name"]) for o in cat["options"]), default=0)
        btn_width = max(12, min(30, longest + 2))  

        for opt in cat["options"]:
            name = opt["name"]
            b = tk.Button(
                self.options_frame,
                text=name,
                width=btn_width,
                command=lambda n=name: self.record_vote(n)
            )
            b.pack(side="left", padx=4, pady=2)

        self.lbl_progress.config(text=f"Category {self.index + 1} of {len(self.data)}")




    def record_vote(self, name):
        # This method records the user's vote and displays appropriate messageboxes.
        # See Point 2 of the "Methods in the GUI class of omg.py" section of the assignment brief.
        pass



# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
