# pip install pysimplegui

# tkinker is the application for creating GUI
from ctypes import alignment
import tkinter as tk

# To create a window popup
window = tk.Tk()

# Define a instructions that could be added to the window
frame_ins = tk.Frame() # Creating frame for instructions
frame_ins.pack()

greeting = tk.Label(
    text="Hello, welcome to Mad Libs",
    # foreground = "white", #set the text color to white
    # background = "black", #set background color to black
    master = frame_ins
)
instructions = tk.Label(text="Add words to the following promps and press play")

# Add the label previously defined to the window
greeting.pack() # pack size the window to only encompass the widget
instructions.pack()

# Create an Entry spot where only 1 line can be added
def createentry(entrytxt):
    entry1 = tk.Label(text= entrytxt)
    entryspace = tk.Entry(window)
    entry1.pack()
    entryspace.pack()
    return entryspace # RETURN HERE SO THAT IT HAS SOMETHING TO CALL ON E.G "GET" FUNCTION

name = createentry("Name")
game = createentry("Enter a game")
city = createentry("Enter a city")
player = createentry("Enter name of a player")
drink = createentry("Enter a name of a drink")
snack = createentry("Enter a snack") 

# Create a function which executes what happens when button is clicked

def openNewWindow(val1,val2,val3,val4,val5,val6):
    # Toplevel object which will 
    # be treated as a new window
    newWindow = tk.Toplevel(window)
 
    # # sets the title of the
    # # Toplevel widget
    newWindow.title("Result")
 
    # # A Label widget to show in toplevel
    tk.Label(
        newWindow,
        text = f'''
        One day me and my friend {val1} decided to play a {val2} game in {val3}. 
        But we were not able to play. So, we went to the game and watched our favourite player {val4}. 
        We drank {val5} and also ate some {val6}. We really enjoyed it! We are looking forward to go again and enjoy'''
        ).pack()

def handle_click():
    r1 = name.get()
    r2 = game.get()
    r3 = city.get()
    r4 = player.get()
    r5 = drink.get()
    r6 = snack.get()
   
    # print("entry1val")
    openNewWindow(r1,r2,r3,r4,r5,r6)

# Create button
playbutton = tk.Button(
    window,
    text="Play",
    bg = "green",
    fg = "white",
    command = handle_click).pack()
# playbutton.bind("<Button-1>", handle_click)
# playbutton.pack()

# this tells Python to run Tkinker in a loop. This method listens for events
 # such as button clicks or keypresses, and blocks any codes that comes after it
 # from running until you close the window when you called the method
window.mainloop()


