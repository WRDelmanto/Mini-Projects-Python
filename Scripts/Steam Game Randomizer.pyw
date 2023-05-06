from tkinter import *
import os
import random


def openSelectGameWindow():
    # Define the path to the Steam game directory
    Steam_Path = 'Z:\SteamLibrary\steamapps\common'

    # Create the window
    window = Tk()

    # Set the window title
    window.title("Random Game")

    # Set the window size
    window.geometry('500x400')

    # Create labels for the selected game
    label = Label(window, text="Today's Game:", font=("Arial Bold", 20))
    label.place(x=250, y=50, anchor=CENTER)

    label1 = Label(window, text='******', width=60, font=("Arial", 10))
    label1.place(x=250, y=200, anchor=CENTER)

    label2 = Label(window, text="Steam Path:", font=("Arial Bold", 14))
    label2.place(x=100, y=375, anchor=CENTER)

    # Create an entry field for the Steam directory path
    input = Entry(window, width=45, font=("Arial", 8))
    input.place(x=325, y=375, anchor=CENTER)
    input.insert(0, Steam_Path)

    # Define a function to select a random game
    def select_game():
        steam_path = input.get()

        games = []

        for entry in os.listdir(steam_path):
            if os.path.isdir(os.path.join(steam_path, entry)):
                games.append(entry)

        random_number = random.randrange(0, len(games) - 1)

        label1.config(text=games[random_number])

    # Create a button to select a random game
    btn = Button(window, text="Click Here!", command=select_game)
    btn.place(x=250, y=300, anchor=CENTER)

    # Keep the window open
    window.mainloop()


openSelectGameWindow()
