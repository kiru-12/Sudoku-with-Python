import random, time, pickle, os, datetime
from tkinter import *
from tkinter import filedialog

def start():
    # clearing root
    children = root.winfo_children()
    for child in children:
        child.destroy()

    root.title('Let the Game Begin')
    # Title and byline
    title = Label(root, text='SUDOKU', font=('Skia', 80), fg='gold', bg='DarkOrchid2', pady=32)
    byline = Label(root, text='by Sai, Sanjay and Kiru', font=('Copperplate', 21), fg='lemon chiffon',
                   bg='DarkOrchid2', pady=21)

    # Three buttons to be displayed
    playButton = Button(root, text='PLAY', font=('Phosphate Solid', 40), fg='firebrick2',
                        bg='DarkOrchid2', pady=10, command=play, highlightthickness=0)
    leaderboardButton = Button(root, text='LEADERBOARD', font=('Phosphate Solid', 40), fg='RoyalBlue2',
                               bg='DarkOrchid2', pady=10, command=leaderboard, highlightthickness=0)
    solverButton = Button(root, text='SOLVER', font=('Phosphate Solid', 40), fg='green',
                          bg='DarkOrchid2', pady=10, command=sudokusolver, highlightthickness=0)

    footer = Label(root, text='© ALL RIGHTS RESERVED', pady=50, font=('Arial', 10), bg='DarkOrchid2')

    # Packing all widgets on to root
    title.pack()
    byline.pack()
    playButton.pack()
    leaderboardButton.pack()
    solverButton.pack()
    footer.pack()

    root.config(bg='DarkOrchid2')

    root.mainloop()


def play():
    # terminating the stopwatch
    try:
        root.after_cancel(stopwatch)
    except:
        pass

    global endtime, s, m, h
    # resetting seconds, minutes and hours all to 0
    s = 0
    m = 0
    h = 0
    # clearing the window
    children = root.winfo_children()
    for child in children:
        child.destroy()

    colour = 'bisque2'
    root.config(bg=colour)
    
    easy = [
        [[0, 4, 8, 2, 0, 0, 0, 0, 1],
         [1, 0, 0, 3, 8, 4, 7, 2, 6],
         [3, 0, 0, 7, 0, 1, 9, 4, 8],
         [0, 7, 2, 6, 4, 5, 1, 8, 0],
         [8, 0, 0, 0, 0, 2, 4, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 7],
         [0, 8, 4, 0, 0, 0, 3, 0, 0],
         [6, 0, 0, 4, 1, 0, 0, 0, 2],
         [0, 0, 3, 0, 0, 0, 0, 7, 4]],

        [[0, 0, 2, 0, 8, 0, 0, 6, 0],
         [0, 5, 6, 9, 1, 7, 0, 3, 0],
         [0, 4, 0, 0, 5, 0, 8, 7, 1],
         [0, 9, 0, 0, 0, 0, 6, 0, 0],
         [6, 7, 1, 0, 9, 5, 2, 0, 0],
         [0, 0, 0, 0, 2, 0, 1, 0, 0],
         [1, 6, 7, 0, 3, 0, 5, 9, 0],
         [4, 8, 0, 0, 7, 0, 3, 0, 0],
         [0, 2, 5, 4, 6, 0, 0, 0, 0]],

        [[0, 7, 9, 8, 0, 2, 0, 6, 3],
         [6, 0, 0, 9, 0, 0, 0, 1, 0],
         [8, 0, 3, 0, 7, 0, 0, 0, 2],
         [0, 9, 0, 0, 0, 0, 3, 7, 1],
         [0, 6, 8, 7, 0, 0, 0, 9, 0],
         [0, 3, 1, 0, 2, 0, 5, 8, 0],
         [2, 8, 6, 5, 0, 0, 1, 3, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [9, 0, 4, 3, 0, 0, 8, 2, 7]],

        [[9, 0, 3, 5, 0, 6, 0, 1, 4],
         [0, 6, 5, 7, 0, 0, 0, 0, 0],
         [1, 0, 7, 0, 0, 0, 5, 0, 0],
         [3, 9, 0, 0, 2, 0, 0, 0, 5],
         [0, 5, 0, 3, 0, 0, 0, 7, 6],
         [0, 8, 1, 4, 0, 0, 2, 9, 3],
         [5, 3, 0, 9, 0, 4, 0, 0, 0],
         [4, 0, 0, 6, 5, 0, 9, 0, 0],
         [0, 7, 0, 0, 3, 0, 4, 0, 2]],

        [[0, 4, 8, 2, 0, 0, 0, 0, 1],
         [1, 0, 0, 3, 8, 4, 7, 2, 6],
         [3, 0, 0, 7, 0, 1, 9, 4, 8],
         [0, 7, 2, 6, 4, 5, 1, 8, 0],
         [8, 0, 0, 0, 0, 2, 4, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 7],
         [0, 8, 4, 0, 0, 0, 3, 0, 0],
         [6, 0, 0, 4, 1, 0, 0, 0, 2],
         [0, 0, 3, 0, 0, 0, 0, 7, 4]]
    ]

    medium = [
        [[9, 0, 0, 8, 4, 1, 3, 0, 0],
         [0, 0, 1, 9, 0, 0, 4, 2, 0],
         [0, 0, 0, 2, 0, 0, 0, 1, 0],
         [8, 7, 0, 1, 0, 0, 5, 4, 0],
         [1, 5, 0, 3, 6, 0, 0, 0, 2],
         [2, 0, 0, 0, 0, 0, 7, 6, 0],
         [7, 2, 0, 0, 0, 5, 1, 9, 0],
         [6, 3, 0, 0, 0, 0, 2, 0, 7],
         [0, 1, 5, 7, 0, 2, 0, 0, 8]],

        [[0, 4, 0, 0, 7, 0, 0, 9, 5],
         [0, 6, 0, 0, 2, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 9, 0, 0, 2],
         [7, 0, 0, 0, 1, 0, 0, 8, 0],
         [3, 0, 0, 5, 0, 8, 0, 0, 7],
         [0, 9, 0, 0, 3, 0, 0, 0, 6],
         [1, 0, 0, 4, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 8, 0, 0, 3, 0],
         [2, 3, 0, 0, 6, 0, 0, 1, 0]],

        [[1, 0, 0, 0, 0, 0, 0, 0, 6],
         [0, 0, 6, 0, 2, 0, 7, 0, 0],
         [7, 8, 9, 4, 5, 0, 1, 0, 3],
         [0, 0, 0, 8, 0, 7, 0, 0, 4],
         [0, 0, 0, 0, 3, 0, 0, 0, 0],
         [0, 9, 0, 0, 0, 4, 2, 0, 1],
         [3, 1, 2, 9, 7, 0, 0, 4, 0],
         [0, 4, 0, 0, 1, 2, 0, 7, 8],
         [9, 0, 8, 0, 0, 0, 0, 0, 0]],

        [[0, 0, 0, 7, 9, 0, 0, 3, 4],
         [5, 0, 9, 2, 0, 0, 0, 1, 8],
         [0, 3, 0, 6, 0, 0, 0, 0, 0],
         [2, 4, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 8, 0, 4, 0, 9, 0, 0],
         [0, 0, 0, 0, 0, 6, 0, 4, 7],
         [0, 0, 0, 0, 0, 8, 0, 2, 0],
         [1, 8, 0, 0, 0, 2, 4, 0, 3],
         [4, 7, 0, 0, 1, 3, 0, 0, 0]],

        [[8, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 3, 6, 0, 0, 0, 0, 0],
         [0, 7, 0, 0, 9, 0, 2, 0, 0],
         [0, 5, 0, 0, 0, 7, 0, 0, 0],
         [0, 0, 0, 0, 4, 5, 7, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 3, 0],
         [0, 0, 1, 0, 0, 0, 0, 6, 8],
         [0, 0, 8, 5, 0, 0, 0, 1, 0],
         [0, 9, 0, 0, 0, 0, 4, 0, 0]],

        [[0, 0, 0, 0, 5, 0, 0, 0, 0],
         [9, 0, 6, 0, 0, 0, 3, 0, 7],
         [0, 0, 0, 4, 0, 9, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 5, 0],
         [2, 0, 0, 6, 0, 7, 0, 0, 1],
         [0, 4, 0, 0, 0, 0, 0, 9, 0],
         [0, 0, 0, 7, 0, 1, 0, 0, 0],
         [7, 0, 9, 0, 0, 0, 2, 0, 6],
         [0, 0, 0, 0, 3, 0, 0, 0, 0]],

        [[0, 0, 4, 7, 1, 0, 0, 0, 0],
         [0, 7, 2, 8, 0, 6, 5, 0, 0],
         [0, 0, 0, 0, 0, 5, 0, 0, 7],
         [0, 1, 0, 6, 9, 0, 2, 0, 0],
         [3, 9, 0, 0, 5, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 8, 5],
         [0, 0, 1, 2, 3, 0, 8, 0, 4],
         [0, 0, 3, 5, 0, 4, 0, 0, 2],
         [2, 4, 0, 9, 0, 0, 0, 0, 0]],

        [[0, 0, 4, 6, 0, 5, 8, 0, 0],
         [6, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 4, 7, 6, 0, 5],
         [2, 8, 0, 3, 0, 0, 0, 0, 0],
         [7, 4, 0, 0, 0, 8, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 9, 0, 0],
         [0, 2, 5, 7, 0, 0, 3, 6, 0],
         [4, 3, 0, 0, 2, 0, 0, 8, 0],
         [0, 0, 0, 8, 6, 3, 5, 4, 0]]

    ]

    hard = [
        [[9, 0, 0, 0, 0, 3, 0, 0, 0],
         [2, 0, 7, 0, 9, 0, 8, 0, 0],
         [0, 0, 0, 0, 0, 2, 5, 9, 0],
         [3, 0, 0, 0, 0, 6, 0, 0, 0],
         [0, 0, 0, 0, 5, 0, 7, 3, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 2],
         [8, 0, 2, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 8, 0, 3, 0, 0],
         [0, 9, 0, 7, 3, 5, 0, 4, 0]],

        [[0, 0, 2, 0, 0, 7, 0, 0, 0],
         [0, 6, 0, 9, 0, 0, 4, 0, 0],
         [0, 9, 0, 2, 5, 0, 0, 0, 3],
         [0, 0, 0, 4, 0, 0, 1, 0, 0],
         [7, 3, 0, 0, 6, 0, 0, 0, 0],
         [0, 0, 9, 5, 3, 0, 0, 6, 0],
         [0, 0, 6, 3, 4, 0, 0, 7, 0],
         [8, 0, 0, 0, 0, 0, 0, 0, 9],
         [0, 0, 0, 0, 0, 0, 0, 5, 0]],

        [[0, 7, 0, 5, 3, 0, 0, 0, 0],
         [8, 0, 1, 6, 0, 0, 2, 0, 7],
         [0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 4, 0, 6, 0, 0, 0],
         [3, 0, 0, 0, 0, 0, 7, 4, 5],
         [0, 8, 0, 0, 0, 0, 0, 0, 6],
         [4, 0, 5, 0, 0, 0, 0, 7, 0],
         [0, 0, 3, 1, 0, 0, 0, 2, 9],
         [0, 0, 0, 0, 0, 0, 5, 0, 0]],

        [[0, 6, 0, 0, 0, 4, 0, 0, 3],
         [0, 0, 0, 3, 0, 0, 0, 5, 0],
         [3, 4, 0, 0, 1, 9, 0, 0, 7],
         [0, 0, 5, 0, 0, 0, 4, 0, 0],
         [7, 0, 0, 8, 0, 0, 0, 0, 2],
         [0, 1, 9, 0, 0, 0, 0, 3, 0],
         [0, 2, 6, 0, 0, 8, 0, 0, 5],
         [8, 5, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 9, 0]],

        [[0, 7, 0, 0, 0, 0, 0, 3, 2],
         [0, 0, 0, 0, 0, 0, 7, 0, 0],
         [2, 0, 0, 0, 5, 0, 0, 9, 0],
         [6, 0, 0, 0, 0, 0, 9, 0, 0],
         [8, 1, 0, 6, 4, 9, 0, 0, 7],
         [0, 0, 4, 8, 0, 0, 0, 0, 3],
         [0, 0, 1, 0, 0, 2, 0, 0, 0],
         [0, 0, 0, 1, 8, 5, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 5, 6, 0]],
    ]

    expert = [
        [[0, 0, 0, 1, 0, 0, 0, 7, 0],
         [0, 3, 0, 0, 0, 0, 0, 6, 0],
         [0, 0, 2, 0, 6, 4, 5, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 4, 0],
         [0, 5, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 2, 0, 6, 8, 9, 1],
         [0, 0, 0, 9, 0, 0, 0, 0, 7],
         [8, 6, 5, 0, 2, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 3, 0, 0, 0]],

        [[5, 8, 6, 4, 0, 0, 0, 0, 3],
         [0, 0, 0, 0, 8, 0, 0, 0, 4],
         [0, 0, 0, 9, 0, 0, 0, 0, 7],
         [0, 0, 0, 0, 0, 0, 0, 4, 0],
         [0, 0, 0, 0, 0, 9, 7, 2, 0],
         [0, 3, 0, 0, 5, 0, 0, 0, 1],
         [7, 0, 0, 0, 0, 0, 0, 6, 0],
         [0, 5, 0, 0, 3, 2, 0, 0, 0],
         [2, 0, 0, 0, 6, 0, 0, 0, 0]],

        [[0, 0, 6, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 8, 7, 0, 6, 0, 9],
         [0, 0, 1, 0, 5, 0, 0, 0, 0],
         [0, 0, 0, 7, 0, 4, 0, 0, 0],
         [0, 7, 9, 0, 0, 2, 5, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 3, 0],
         [0, 1, 0, 0, 0, 0, 0, 6, 0],
         [0, 8, 0, 0, 1, 0, 0, 0, 3],
         [0, 0, 4, 0, 0, 3, 0, 9, 0]],

        [[0, 0, 0, 0, 4, 5, 0, 0, 0],
         [0, 0, 0, 0, 2, 6, 0, 0, 0],
         [0, 0, 0, 0, 9, 0, 0, 3, 7],
         [4, 0, 0, 9, 0, 0, 0, 8, 0],
         [9, 1, 5, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 3, 2, 0, 0, 0, 6, 5, 0],
         [7, 0, 0, 0, 0, 0, 2, 0, 0],
         [0, 0, 0, 1, 6, 0, 0, 4, 0]],

        [[0, 1, 0, 0, 0, 8, 0, 0, 6],
         [3, 6, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 5, 0, 0, 0, 0, 7],
         [0, 0, 0, 0, 8, 4, 5, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [9, 0, 5, 0, 1, 3, 8, 0, 0],
         [0, 0, 2, 0, 9, 0, 0, 0, 0],
         [0, 0, 3, 7, 0, 0, 0, 0, 0],
         [7, 0, 0, 0, 0, 0, 4, 0, 0]]

    ]

    insanelyextreme = [
        [[0, 0, 2, 0, 0, 1, 0, 0, 6],
         [0, 5, 0, 0, 6, 0, 0, 2, 0],
         [8, 0, 0, 9, 0, 0, 5, 0, 0],
         [3, 0, 0, 8, 0, 0, 9, 0, 0],
         [0, 8, 0, 0, 5, 0, 0, 6, 0],
         [0, 0, 4, 0, 0, 7, 0, 0, 3],
         [0, 0, 3, 0, 0, 4, 0, 0, 8],
         [0, 7, 0, 0, 8, 0, 0, 1, 0],
         [1, 0, 0, 2, 0, 0, 4, 0, 0]],

        [[0, 0, 7, 0, 0, 0, 0, 0, 0],
         [0, 6, 0, 8, 9, 0, 1, 4, 0],
         [0, 9, 0, 0, 0, 2, 0, 0, 6],
         [0, 0, 3, 5, 0, 9, 0, 6, 0],
         [0, 8, 0, 0, 0, 0, 0, 9, 0],
         [0, 1, 0, 4, 0, 3, 8, 0, 0],
         [7, 0, 0, 3, 0, 0, 0, 1, 0],
         [0, 5, 8, 0, 4, 1, 0, 7, 0],
         [0, 0, 0, 0, 0, 0, 9, 0, 0]],

        [[0, 0, 8, 0, 0, 1, 0, 0, 2],
         [0, 4, 0, 0, 3, 0, 0, 1, 0],
         [6, 0, 0, 7, 0, 0, 4, 0, 0],
         [5, 0, 0, 3, 0, 0, 2, 0, 0],
         [0, 9, 0, 0, 7, 0, 0, 4, 0],
         [0, 0, 4, 0, 0, 9, 0, 0, 1],
         [0, 0, 3, 0, 0, 8, 0, 0, 6],
         [0, 7, 0, 0, 4, 0, 0, 8, 0],
         [1, 0, 0, 2, 0, 0, 3, 0, 0]],

        [[0, 3, 0, 0, 6, 0, 0, 7, 0],
         [5, 0, 0, 3, 0, 9, 0, 0, 1],
         [0, 0, 9, 0, 0, 0, 5, 0, 0],
         [0, 8, 0, 0, 4, 0, 0, 6, 0],
         [4, 0, 0, 8, 0, 6, 0, 0, 9],
         [0, 2, 0, 0, 3, 0, 0, 8, 0],
         [0, 0, 2, 0, 0, 0, 8, 0, 0],
         [6, 0, 0, 1, 0, 8, 0, 0, 4],
         [0, 9, 0, 0, 7, 0, 0, 5, 0]],

        [[0, 0, 9, 7, 0, 0, 0, 0, 1],
         [0, 3, 0, 0, 8, 0, 0, 4, 0],
         [8, 0, 0, 0, 0, 4, 2, 0, 0],
         [6, 0, 0, 0, 0, 9, 3, 0, 0],
         [0, 9, 0, 0, 7, 0, 0, 6, 0],
         [0, 0, 7, 5, 0, 0, 0, 0, 4],
         [0, 0, 2, 8, 0, 0, 0, 0, 9],
         [0, 5, 0, 0, 6, 0, 0, 2, 0],
         [3, 0, 0, 0, 0, 2, 5, 0, 0]]
    ]
    
    # separation frames
    top = Frame(root, bg=colour)
    left = Frame(root, width=70, bg=colour)
    mid = Frame(root, bg=colour)
    mid2 = Frame(root, bg=colour)
    bottom = Frame(root, bg=colour)

    # label asking for user name
    name = Label(root, text='Enter your name', font=('Futura Condensed Medium', 35), bg=colour)
    # entry box for user to enter name
    global userName, playername
    userName = Entry(root, width=30, font=('Futura Condensed Medium', 35), justify='center', fg='red',
                     bg=colour, highlightthickness=0)
    playername = userName.get()

    # label prompting the user to choose difficulty level by clicking the corresponding button
    options = Label(root, text='Choose difficulty level', font=('Futura Condensed Medium', 35), bg=colour)
    easyB = Button(root, text='Easy', bg='coral1', fg='blue', font=('Futura Condensed Medium', 30),
                   command=lambda: drawgrid(easy, 'Easy'), highlightthickness=0)
    mediumB = Button(root, text='Medium', bg='tomato2', fg='RoyalBlue3', font=('Futura Condensed Medium', 30),
                     command=lambda: drawgrid(medium, 'Medium'), highlightthickness=0)
    hardB = Button(root, text='Hard', bg='firebrick2', fg='DeepSkyBlue3', font=('Futura Condensed Medium', 30),
                   command=lambda: drawgrid(hard, 'Hard'), highlightthickness=0)
    expertB = Button(root, text='Expert', bg='red2', fg='cornflower blue', font=('Futura Condensed Medium', 30),
                     command=lambda: drawgrid(expert, 'Expert'), highlightthickness=0)
    insanelyextremeB = Button(root, text='Insanely Extreme', bg='red3', fg='sky blue',
                              font=('Futura Condensed Medium', 30),
                              command=lambda: drawgrid(insanelyextreme, 'Insanely Extreme'), highlightthickness=0)

    # button to go back to previous window
    home = Button(root, text='Home', font=('Helvetica Neue Bold', 20), command=start, bg=colour, highlightthickness=0)

    # placing all widgets on grid
    top.grid(row=0, padx=20, pady=30)
    left.grid(column=0)
    name.grid(row=1, column=1, columnspan=5)
    userName.grid(row=2, column=1, columnspan=5)

    mid.grid(row=3, padx=20, pady=20)

    options.grid(row=4, column=1, columnspan=5)
    mid2.grid(row=5, column=2, padx=20, pady=20)

    easyB.grid(row=6, column=1)
    mediumB.grid(row=6, column=2)
    hardB.grid(row=6, column=3)
    expertB.grid(row=6, column=4)
    insanelyextremeB.grid(row=6, column=5)

    bottom.grid(row=7, column=2, padx=20, pady=70)
    home.grid(row=8, column=4)


def leaderboard():
    # clearing the window
    global root
    children = root.winfo_children()
    for child in children:
        child.destroy()

    root.config(bg='navy')

    title = Label(root, text='LEADERBOARD', font=('Futura Condensed Medium', 40), bg='orange red')
    title.pack()

    fr = Frame(root, height=200, width=200, bg='lawn green')
    fr.pack()

    left = Frame(fr, height=20, width=20, bg='lawn green')
    left.grid(row=0, column=0, padx=15)
    name = Label(left, text='Name', font=('Futura Condensed Medium', 30), bg='lawn green')
    name.pack()

    middle = Frame(fr, height=20, width=20, bg='lawn green')
    middle.grid(row=0, column=1, padx=20)
    tt = Label(middle, text='Time Taken', font=('Futura Condensed Medium', 30), bg='lawn green')
    tt.pack()

    right = Frame(fr, height=20, width=20, bg='lawn green')
    right.grid(row=0, column=2, padx=20)
    dif = Label(right, text='Difficulty Level', font=('Futura Condensed Medium', 30), bg='lawn green')
    dif.pack()

    homebutton = Button(root, text='Home', command=start, fg='yellow', bg='cyan')
    homebutton.pack()

    tbl1 = []
    tbl2 = []
    tbl3 = []

    filehandle = open('leaderboard.dat','rb')

    while True:
        try:
            details = pickle.load(filehandle)
            tbl1.append(details[0])
            tbl2.append(details[1])
            tbl3.append(details[2])

        except EOFError:
            break

    filehandle.close()

    for i in tbl1:
        dsp = Label(left, text=i, font=('Futura Condensed Medium', 25), bg='lawn green')
        dsp.pack()
    for i in tbl2:
        dsp = Label(middle, text=i, font=('Futura Condensed Medium', 25), bg='lawn green')
        dsp.pack()
    for i in tbl3:
        dsp = Label(right, text=i, font=('Futura Condensed Medium', 25), bg='lawn green')
        dsp.pack()


def sudokusolver():
    global root, usr
    children = root.winfo_children()
    for child in children:
        child.destroy()

    colour = 'OliveDrab1'
    root.config(bg=colour)

    # Function to reveal the solution
    def ss_reveal():
        try:
            starting = time.time()
            global entry_list
            for y in range(9):
                for x in range(9):
                    entry_list[y][x].config(text='')
            for y in range(9):
                for x in range(9):
                    usr[y][x] = entry_list[y][x].get()

            # since all elements in usr, here all are converted into integers
            for y in range(9):
                for x in range(9):
                    if usr[y][x] != '':
                        usr[y][x] = int(usr[y][x])
                    else:
                        usr[y][x] = 0

            def ss_possible(y, x, n):
                global usr
                for i in range(9):
                    if usr[y][i] == n:
                        return False

                for i in range(9):
                    if usr[i][x] == n:
                        return False
                tempx = (x // 3) * 3
                tempy = (y // 3) * 3
                for i in range(3):
                    for j in range(3):
                        if usr[tempy + i][tempx + j] == n:
                            return False
                return True

            def ss_solve():
                global usr, root
                ending = time.time()
                if ((ending - starting) % 60) > 30:
                    children = root.winfo_children()
                    for child in children:
                        child.destroy()
                    error = Label(root, text='ERROR 408', font=('AppleGothic', 50), fg='red')
                    error.pack()
                    message = Label(root, text='Request Timeout.\nPlease verify puzzle before entering into the grid.',
                                    font=('AppleGothic', 20))
                    message.pack()
                    back = Button(root, text='Home', command=start)
                    back.pack()
                else:
                    for y in range(9):
                        for x in range(9):
                            if usr[y][x] == 0:
                                for n in range(1, 10):
                                    if ss_possible(y, x, n):
                                        usr[y][x] = n
                                        ss_solve()
                                        usr[y][x] = 0
                                return
                    # The solved puzzle is displayed on the grid
                    for y in range(9):
                        for x in range(9):
                            entry_list[y][x].delete(0, END)
                            entry_list[y][x].insert(0, usr[y][x])
                            entry_list[y][x].config(state='disabled',
                                                    disabledbackground=colour, disabledforeground='grey40')

            ss_solve()

        except ValueError:
            error_message = Label(root, text='Make sure there are no text literals in the grid!', fg='red')
            error_message.grid(row=11, column=2, columnspan=8)
    # Function to save a puzzle
    def save():
       
        try:
            global entry_list
            for y in range(9):
                for x in range(9):
                    entry_list[y][x].config(text='')
            for y in range(9):
                for x in range(9):
                    usr[y][x] = entry_list[y][x].get()

            # since all elements in usr, here all are converted into integers
            for y in range(9):
                for x in range(9):
                    if usr[y][x] != '':
                        usr[y][x] = int(usr[y][x])
                    else:
                        usr[y][x] = 0
        except ValueError:
            error_message = Label(root, text='Make sure there are no text literals in the grid!',
                                  fg='red', highlightthickness=0, bg=colour)
            error_message.grid(row=11, column=2, columnspan=8)

        def write(name):
            filehandle = open(f'savedpuzzles/{name}.dat', 'wb')
            pickle.dump(usr, filehandle)
            filehandle.flush()
            filehandle.close()

            children = win.winfo_children()
            for child in children:
                child.destroy()
            lbl = Label(win, text='Your puzzle has been saved.').pack()

        win = Tk()
        win.geometry('250x100')
        win.title('Save Puzzle')
        l = Label(win, text='Enter name for puzzle:')
        puzname = Entry(win, width=25)
        dt  = datetime.datetime.now()
        
        if puzname.get() == '':
            pn = dt
        else:
            pn = puzname.get()
            
        saveB = Button(win, text='Save', command=lambda:write(pn))
        l.pack()
        puzname.pack()
        saveB.pack()
        win.mainloop()
        
    # Function to open a saved puzzle
    def openpuz():
        for y in range(9):
            for x in range(9):
                entry_list[y][x].config(state='normal')
                entry_list[y][x].delete(0, END)

        root.filename = filedialog.askopenfilename(initialdir='savedpuzzles', title='Select a File')
        try:
            filehandle = open(root.filename, 'rb')
        except FileNotFoundError:
            return
        temp = pickle.load(filehandle)

        for y in range(9):
            for x in range(9):
                if temp[y][x] != 0:
                    entry_list[y][x].insert(0, str(temp[y][x]))
                if temp[y][x] == 0:
                    entry_list[y][x].delete(0, END)

        filehandle.close()
    # Function to clear the grid
    def clear():
        for y in range(9):
            for x in range(9):
                entry_list[y][x].config(state='normal')
                entry_list[y][x].delete(0, END)

    # i = row and j = column
    global entry_list, horiseparators, vertseparators
    for i in range(9):
        for j in range(9):
            if i in (3, 7):
                for u in range(3):
                    if j in (0, 1, 2):
                        horiseparators[u] = Label(root, text='------', bg=colour)
                        horiseparators[u].grid(row=i, column=j)
                    if j in (3, 4, 5):
                        horiseparators[u] = Label(root, text='------', bg=colour)
                        horiseparators[u].grid(row=i, column=j + 1)
                    if j in (6, 7, 8):
                        horiseparators[u] = Label(root, text='------', bg=colour)
                        horiseparators[u].grid(row=i, column=j + 2)

            if j in (3, 7):
                for v in range(3):
                    vertseparators[v] = Canvas(root, width=5, height=20, highlightthickness=0, bg=colour)
                    vertseparators[v].grid(column=j)

            if i in (0, 1, 2):
                if j in (0, 1, 2):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             highlightthickness=0, bg=colour)
                    entry_list[i][j].grid(row=i, column=j)
                if j in (3, 4, 5):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             highlightthickness=0, bg=colour)
                    entry_list[i][j].grid(row=i, column=j + 1)
                if j in (6, 7, 8):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             highlightthickness=0, bg=colour)
                    entry_list[i][j].grid(row=i, column=j + 2)
            if i in (3, 4, 5):
                if j in (0, 1, 2):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             highlightthickness=0, bg=colour)
                    entry_list[i][j].grid(row=i + 1, column=j)
                if j in (3, 4, 5):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             highlightthickness=0, bg=colour)
                    entry_list[i][j].grid(row=i + 1, column=j + 1)
                if j in (6, 7, 8):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             highlightthickness=0, bg=colour)
                    entry_list[i][j].grid(row=i + 1, column=j + 2)
            if i in (6, 7, 8):
                if j in (0, 1, 2):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             highlightthickness=0, bg=colour)
                    entry_list[i][j].grid(row=i + 2, column=j)
                if j in (3, 4, 5):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             highlightthickness=0, bg=colour)
                    entry_list[i][j].grid(row=i + 2, column=j + 1)
                if j in (6, 7, 8):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             highlightthickness=0, bg=colour)
                    entry_list[i][j].grid(row=i + 2, column=j + 2)

    # Separation between the grid and the set of buttons
    ss_rightsep = Canvas(root, width=12, height=20, highlightthickness=0, bg=colour)
    ss_rightsep.grid(column=11)

    ss_revealButton = Button(root, text='Reveal Solution', command=ss_reveal, width=12, height=2,
                             highlightthickness=0, bg=colour)
    ss_revealButton.grid(row=4, column=12)

    ss_openButton = Button(root, text='Open', command=openpuz, width=12, height=2, highlightthickness=0, bg=colour)
    ss_openButton.grid(row=5, column=12)

    ss_saveButton = Button(root, text='Save', command=save, width=12, height=2, highlightthickness=0, bg=colour)
    ss_saveButton.grid(row=6, column=12)

    ss_clearButton = Button(root, text='Clear', command=clear, width=12, height=2, highlightthickness=0, bg=colour)
    ss_clearButton.grid(row=8, column=12)

    ss_backButton = Button(root, text='Go Back', command=start, width=12, height=2, highlightthickness=0, bg=colour)
    ss_backButton.grid(row=9, column=12)


def win(tag):
    colour = 'khaki1'
    root.config(bg=colour)
    root.title('Mazel Tov!')
    # clearing the window to build the next page
    children = root.winfo_children()
    for child in children:
        child.destroy()

    seconds = int((endtime - starttime) % 60)
    minutes = int((endtime - starttime) // 60)

    global cursor, playername
    if (seconds < 10) and (minutes < 10):
        time_taken = f'0{minutes}:0{seconds}'
    if (seconds >= 10) and (minutes < 10):
        time_taken = f'0{minutes}:{seconds}'
    if (seconds < 10) and (minutes >= 10):
        time_taken = f'{minutes}:0{seconds}'
    if (seconds >= 10) and (minutes >= 10):
        time_taken = f'{minutes}:{seconds}'

    filehandle = open('leaderboard.dat', 'ab')
    templist = [f'{playername}', f'{time_taken}', f'{tag}']
    pickle.dump(templist, filehandle)
    filehandle.flush()
    filehandle.close()

    wincan = Canvas(root, height=515, width=515, bg=colour, highlightthickness=0)
    wincan.create_oval(60, 50, 460, 450, fill='lawn green', outline='aquamarine')
    wincan.create_text(265, 180, text=f'Great work, {playername}! ', font=('Helvetica', 17))
    wincan.create_text(265, 240, text='YOU WIN', font=('Helvetica', 50))
    wincan.create_text(265, 300, text=f'You took {minutes} minutes and {seconds} seconds to complete')
    wincan.pack()

    homebutton = Button(root, text='Home', command=start)
    homebutton.pack()


def lose():
    colour = 'khaki1'
    root.config(bg=colour)
    root.title('Tough Luck!')
    # clearing the window to build the next page
    children = root.winfo_children()
    for child in children:
        child.destroy()

    seconds = int((endtime - starttime) % 60)
    minutes = int((endtime - starttime) // 60)

    global playername

    losecan = Canvas(root, height=515, width=515, bg=colour, highlightthickness=0)
    losecan.create_oval(60, 50, 460, 450, fill='brown1', outline='yellow')
    losecan.create_text(265, 180, text=f'Sorry {playername}', font=('Helvetica', 17))
    losecan.create_text(265, 240, text='YOU LOSE', font=('Helvetica', 50))
    losecan.create_text(265, 300, text=f'You took {minutes} minutes and {seconds} seconds', font=('Helvetica', 15))
    losecan.create_text(265, 320, text=f'Better luck next time', font=('Helvetica', 15))
    losecan.pack()

    homebutton = Button(root, text='Home', command=start)
    homebutton.pack()


def possible(y, x, n):
    global puzzle
    for i in range(9):
        if puzzle[y][i] == n:
            return False

    for i in range(9):
        if puzzle[i][x] == n:
            return False
    tempx = (x // 3) * 3
    tempy = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if puzzle[tempy + i][tempx + j] == n:
                return False
    return True


def solve(tag):
    global puzzle
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        puzzle[y][x] = n
                        solve(tag)
                        puzzle[y][x] = 0
                return

    if puzzle == usr:
        win(tag)
    else:
        lose()


def check(tag):
    # getting all values from the entry boxes and putting them into a temporary list usr
    for y in range(9):
        for x in range(9):
            usr[y][x] = entry_list[y][x].get()

    # since all elements in usr are strings, here all are converted into integers
    for y in range(9):
        for x in range(9):
            if usr[y][x] != '':
                try:
                    usr[y][x] = int(usr[y][x])
                except ValueError:
                    error_message = Label(root, text='Make sure that you only enter numbers!',
                                          fg='red', highlightthickness=0, bg='khaki1')
                    error_message.grid(row=11, column=2, columnspan=8)
                    return
            else:
                usr[y][x] = 0

    # terminating the stopwatch
    root.after_cancel(stopwatch)
    # resetting seconds, minutes and hours all to 0
    global endtime, s, m, h
    s = 0
    m = 0
    h = 0
    # getting end time
    endtime = time.time()
    # proceeding to solve
    solve(tag)


def reveal():
    # terminating the stopwatch
    try:
        root.after_cancel(stopwatch)
    except:
        pass
    # resetting seconds, minutes and hours all to 0
    global endtime, s, m, h
    s = 0
    m = 0
    h = 0
    # getting end time
    endtime = time.time()
    # destroying checkButton, revealButton, timelabel and w(i.e. the stopwatch)
    checkButton.destroy()
    revealButton.destroy()
    timelabel.destroy()
    w.destroy()

    # rs_solve() and rs_possible() are identical to solve() and possible() respectively
    # since the solved puzzle lasts only within the solve() function, we are creating
    # rs_solve() and rs_possible() to solve the puzzle right here and display right away
    def rs_possible(y, x, n):
        global puzzle
        for i in range(9):
            if puzzle[y][i] == n:
                return False

        for i in range(9):
            if puzzle[i][x] == n:
                return False
        tempx = (x // 3) * 3
        tempy = (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if puzzle[tempy + i][tempx + j] == n:
                    return False
        return True

    def rs_solve():
        global puzzle
        for y in range(9):
            for x in range(9):
                if puzzle[y][x] == 0:
                    for n in range(1, 10):
                        if rs_possible(y, x, n):
                            puzzle[y][x] = n
                            rs_solve()
                            puzzle[y][x] = 0
                    return
        # The solved puzzle is displayed on the grid
        for y in range(9):
            for x in range(9):
                entry_list[y][x].delete(0, END)
                entry_list[y][x].insert(0, puzzle[y][x])
                entry_list[y][x].config(state='disabled', disabledbackground='khaki1', disabledforeground='grey40')

    rs_solve()


def drawgrid(difficulty, tag):
    # getting the entered name
    global playername
    playername = userName.get()
    if playername == '':
        playername = 'User'
    # clearing root
    global root
    children = root.winfo_children()
    for child in children:
        child.destroy()

    colour = 'khaki1'
    root.config(bg=colour)

    # i = row and j = column
    global entry_list, horiseparators, vertseparators
    for i in range(9):
        for j in range(9):
            if i in (3, 7):
                for u in range(3):
                    # horizontal separators
                    if j in (0, 1, 2):
                        horiseparators[u] = Label(root, text='------', bg=colour)
                        horiseparators[u].grid(row=i, column=j)
                    if j in (3, 4, 5):
                        horiseparators[u] = Label(root, text='------', bg=colour)
                        horiseparators[u].grid(row=i, column=j + 1)
                    if j in (6, 7, 8):
                        horiseparators[u] = Label(root, text='------', bg=colour)
                        horiseparators[u].grid(row=i, column=j + 2)

            # vertical separators
            if j in (3, 7):
                for v in range(3):
                    vertseparators[v] = Canvas(root, width=5, height=20, highlightthickness=0, bg=colour)
                    vertseparators[v].grid(column=j)

            # entry boxes which together make up the grid
            if i in (0, 1, 2):
                if j in (0, 1, 2):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             bg=colour, highlightthickness=0)
                    entry_list[i][j].grid(row=i, column=j)
                if j in (3, 4, 5):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             bg=colour, highlightthickness=0)
                    entry_list[i][j].grid(row=i, column=j + 1)
                if j in (6, 7, 8):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             bg=colour, highlightthickness=0)
                    entry_list[i][j].grid(row=i, column=j + 2)
            if i in (3, 4, 5):
                if j in (0, 1, 2):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             bg=colour, highlightthickness=0)
                    entry_list[i][j].grid(row=i + 1, column=j)
                if j in (3, 4, 5):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             bg=colour, highlightthickness=0)
                    entry_list[i][j].grid(row=i + 1, column=j + 1)
                if j in (6, 7, 8):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             bg=colour, highlightthickness=0)
                    entry_list[i][j].grid(row=i + 1, column=j + 2)
            if i in (6, 7, 8):
                if j in (0, 1, 2):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             bg=colour, highlightthickness=0)
                    entry_list[i][j].grid(row=i + 2, column=j)
                if j in (3, 4, 5):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             bg=colour, highlightthickness=0)
                    entry_list[i][j].grid(row=i + 2, column=j + 1)
                if j in (6, 7, 8):
                    entry_list[i][j] = Entry(root, width=2, font=('Arial', 27), justify='center',
                                             bg=colour, highlightthickness=0)
                    entry_list[i][j].grid(row=i + 2, column=j + 2)

    # Separation between the grid and the set of buttons
    rightsep = Canvas(root, width=12, height=20, bg=colour, highlightthickness=0)
    rightsep.grid(column=11)

    global puzzle
    l = len(difficulty)
    for i in range(l):
        j = random.randint(0, l - 1)
        puzzle = difficulty[j]

    # Displaying the puzzle on the grid
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] != 0:
                entry_list[y][x].insert(0, str(puzzle[y][x]))
                entry_list[y][x].config(disabledforeground='grey40',disabledbackground=colour, state=DISABLED)

    global checkButton, revealButton, backButton, timelabel, clock, stopwatch, starttime, w
    checkButton = Button(root, text='Check', width=12, height=2, command=lambda:check(tag),
                         bg=colour, highlightthickness=0)
    checkButton.grid(row=4, column=12)

    revealButton = Button(root, text='Reveal Solution', command=reveal, width=12, height=2,
                          bg=colour, highlightthickness=0)
    revealButton.grid(row=5, column=12)

    backButton = Button(root, text='Go Back', command=play, width=12, height=2,
                        bg=colour, highlightthickness=0)
    backButton.grid(row=6, column=12)

    timelabel = Label(root, text='Time Elapsed:', font=('Futura Condensed Medium', 27),
                      bg=colour, highlightthickness=0)
    timelabel.grid(row=1, column=12)

    starttime = time.time()

    w = Label(root, font=('Consolas', 23), bg=colour)
    w.grid(row=2, column=12)

    root.after(0, clockrun)


def clockrun():
    global s, m, h

    # Delete old text
    w.config(text='')

    if (s < 10) and (m < 10) and (h < 10):
        # Add new text
        w.config(text="0%s:0%s:0%s" % (h, m, s), font=("Futura Condensed Medium", 27))
    if (s >= 10) and (m < 10) and (h < 10):
        # Add new text
        w.config(text="0%s:0%s:%s" % (h, m, s), font=("Futura Condensed Medium", 27))
    if (s < 10) and (m >= 10) and (h < 10):
        # Add new text
        w.config(text="0%s:%s:0%s" % (h, m, s), font=("Futura Condensed Medium", 27))
    if (s >= 10) and (m >= 10) and (h < 10):
        # Add new text
        w.config(text="0%s:%s:%s" % (h, m, s), font=("Futura Condensed Medium", 27))

    s += 1
    if s == 60:
        m += 1
        s = 0
    elif m == 59:
        h += 1
        m = -1

    # After 1 second, call run again (start an infinite recursive loop)
    global stopwatch
    stopwatch = root.after(1000, clockrun)


# declaring root
root = Tk()
root.geometry('620x550')

# 81 entry boxes
entry00, entry01, entry02, entry03, entry04 = Entry(), Entry(), Entry(), Entry(), Entry()
entry05, entry06, entry07, entry08 = Entry(), Entry(), Entry(), Entry()
entry10, entry11, entry12, entry13, entry14 = Entry(), Entry(), Entry(), Entry(), Entry()
entry15, entry16, entry17, entry18 = Entry(), Entry(), Entry(), Entry()
entry20, entry21, entry22, entry23, entry24 = Entry(), Entry(), Entry(), Entry(), Entry()
entry25, entry26, entry27, entry28 = Entry(), Entry(), Entry(), Entry()
entry30, entry31, entry32, entry33, entry34 = Entry(), Entry(), Entry(), Entry(), Entry()
entry35, entry36, entry37, entry38 = Entry(), Entry(), Entry(), Entry()
entry40, entry41, entry42, entry43, entry44 = Entry(), Entry(), Entry(), Entry(), Entry()
entry45, entry46, entry47, entry48 = Entry(), Entry(), Entry(), Entry()
entry50, entry51, entry52, entry53, entry54 = Entry(), Entry(), Entry(), Entry(), Entry()
entry55, entry56, entry57, entry58 = Entry(), Entry(), Entry(), Entry()
entry60, entry61, entry62, entry63, entry64 = Entry(), Entry(), Entry(), Entry(), Entry()
entry65, entry66, entry67, entry68 = Entry(), Entry(), Entry(), Entry()
entry70, entry71, entry72, entry73, entry74 = Entry(), Entry(), Entry(), Entry(), Entry()
entry75, entry76, entry77, entry78 = Entry(), Entry(), Entry(), Entry()
entry80, entry81, entry82, entry83, entry84 = Entry(), Entry(), Entry(), Entry(), Entry()
entry85, entry86, entry87, entry88 = Entry(), Entry(), Entry(), Entry()

entry_list = [[entry00, entry01, entry02, entry03, entry04, entry05, entry06, entry07, entry08],
              [entry10, entry11, entry12, entry13, entry14, entry15, entry16, entry17, entry18],
              [entry20, entry21, entry22, entry23, entry24, entry25, entry26, entry27, entry28],
              [entry30, entry31, entry32, entry33, entry34, entry35, entry36, entry37, entry38],
              [entry40, entry41, entry42, entry43, entry44, entry45, entry46, entry47, entry48],
              [entry50, entry51, entry52, entry53, entry54, entry55, entry56, entry57, entry58],
              [entry60, entry61, entry62, entry63, entry64, entry65, entry66, entry67, entry68],
              [entry70, entry71, entry72, entry73, entry74, entry75, entry76, entry77, entry78],
              [entry80, entry81, entry82, entry83, entry84, entry85, entry86, entry87, entry88]]

# Separators for the purpose of displaying the grid with gaps
hsep1, hsep2, hsep3 = Label(), Label(), Label()
vsep1, vsep2, vsep3 = Canvas(), Canvas(), Canvas()
horiseparators = [hsep1, hsep2, hsep3]
vertseparators = [vsep1, vsep2, vsep3]

# puzzle is the actual question that will be asked to the user
puzzle = []

# usr is used to receive the user's input
usr = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# seconds, minutes, hours (initially 0)
s = 0
m = 0
h = 0

# creating savedpuzzles directory and leaderboard.dat
path = os.getcwd()
sp = path + '/savedpuzzles'
lb = path + '/leaderboard.dat'
try:
    os.mkdir(sp)
except FileExistsError:
    pass
if os.path.exists(lb):
    pass
else:
    f = open('leaderboard.dat','wb')
    f.close()

# calling start() to initiate the game
start()





