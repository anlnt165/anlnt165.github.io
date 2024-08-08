# Import random and tkinter modules
import random

import tkinter as tk
import string

# Define password generator function
def createpass(n): # input value of characters #
    evenN = round(n/2-1)
    numInt = random.randint(2,evenN)
    # print(numInt)
    numList = []
    while len(numList) < numInt:
        # Generate a random number
        num = random.randint(0,9)
        if num not in numList: # Repeat
            numList.append(num)

    # print(numList)

    charList = []
    while len(charList) < n-numInt:
        # Generate a random character
        char = random.choice(string.ascii_letters)
        if char not in charList: # Repeat
            charList.append(char)

    # # Ensure lowercase and uppercase
    cnt = 0
    for c in charList:
        if c.islower(): # count number of characters that are lowercase
            cnt +=1
    
    if cnt == 0: # If no lowercase or if all are lowercase
        # Select number of character to change to uppercase
        ran_char = random.randint(0,len(charList))
        # Select a random position to change a character to become lowercase
        for i in range(ran_char):
            ran_pos = random.randint(0,len(charList))
            # Change character to uppercase
            charList[ran_pos] = charList[ran_pos].upper()

    elif  cnt == len(charList):
        # Select a random position to change x character to become lowercase
        ran_char = random.randint(0,len(charList))
        # Select a random position to change a character to become lowercase
        for i in range(ran_char):
            ran_pos = random.randint(0,len(charList))
            # Change character to uppercase
            charList[ran_pos] = charList[ran_pos].upper()

    # Combine random character and number
    joinN = ''.join(map(str,numList))
    joinC = ''.join(map(str,charList))

    # Join
    password = joinN + joinC
    shuffle_pass = ''.join(random.sample(password,len(password)))

    return shuffle_pass

# Create widget
window = tk.Tk()

# Enter length of password input
greeting = tk.Label(text = "Python Password Generator")
instruction = tk.Label(text = "Enter Length of password")
entry = tk.Entry(window)

greeting.pack()
instruction.pack()
entry.pack()

# Create handle click function
def handle_click():
    length = entry.get()
    l = int(length)
    password = createpass(l)
    # Provide password
    generate_pass = tk.Label(text = "Your password is " + password)
    generate_pass.pack()
    

# Create Button
generator_button = tk.Button(
    window,
    text="Generate Password",
    bg = "green",
    fg = "white",
    command = handle_click).pack()

window.mainloop()