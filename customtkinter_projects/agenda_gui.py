# Simple Agenda GUI project with SQLite
import sqlite3
from tkinter.constants import BROWSE

import customtkinter as ctk

DB_PATH = "customtkinter_projects/agenda.db"


# DATA
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS contacts (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Phone TEXT,
                Email TEXT,
                Notes TEXT,
                CreatedOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()
    pass



# CustomTkinter

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("system") # "light" | "dark" | "system"
        ctk.set_default_color_theme("blue") # "blue" | "green" | "dark-blue"

        self.title("Agenda - CustomTkinter and SQLite")
        self.geometry("1000x600")
        self.minsize(900, 520)

        #Base layout
        self.grid_columnconfigure(0, weight=2) #List
        self.grid_columnconfigure(1, weight=3) #Form
        self.grid_rowconfigure(1, weight=1)

        #Top bar
        topbar = ctk.CTkFrame(self, corner_radius=12, fg_color="transparent") #Creating a frame(Container) inside the main window(self), corner radius = 12 to define the radius and fg_color = transparent to make the frame transparent
        topbar.grid(row=0, column=1, sticky="ew", padx=12, pady=(12, 6)) # Define the position of the frame inside the main window, the sticky parameter is used to expand the frame when the window is resized (in this case in the horizontal direction)
        topbar.grid_columnconfigure(0, weight=1) #Define the weight of the frame in the column and width in the column

        #Search Entry
        self.search_entry = ctk.CTkEntry(topbar, placeholder_text="Search...") #Creating a text entry widget inside the frame topbar
        self.search_entry.grid(row=0, column=0, sticky="ew", padx=(0, 8), pady=6) #Styling the text entry widget and defining its position, padx is the margin in the horizontal and pady is the margin in the vertical direction

        #Search Button
        self.search_button = ctk.CTkButton(topbar, text= "Search", command=self.on_search)
        self.search_button.grid(row=0, column=1, padx=2)

        #Clear Button
        self.clear_button = ctk.CTkButton(topbar, text= "Clear", command=self.on_clear, fg_color="gray") #Changing the color of the button to gray
        self.clear_button.grid(row=0, column=2, padx=12)

        init_db()
        pass

    def on_search(self):
        pass

    def on_clear(self):
        pass
    pass