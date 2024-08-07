# Import random and tkinter modules
# import random
# import tkinter as tk
# import string

# Define password generator function
def createpass(n): # input value of characters #
    evenN = n/2-1
    numInt = random.randint(2,evenN)
    numList = []
    while len(numList) <= numInt:
        # Generate a random number
        num = random.randint(0,9)
        if num not in numList: # Repeat
            numList.append(num)

    charList = []
    while len(charList) <= n-numInt:
        # Generate a random character
        char = random.choice(string.ascii_letters)
        if char not in charList: # Repeat
            charList.append(char)

    # Combine random character and number
    joinN = ''.join(map(str,numList))
    joinC = ''.join(map(str,charList))

    # # Ensure lowercase and uppercase
    # cnt = 0
    # for c in joinC:
    #     if c.islower():
    #         cnt +=1
    # if cnt == 0:
        

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
    generate_pass = tk.Label(text = "Your password is" + password)
    generate_pass.pack()
    

# Create Button
generator_button = tk.Button(
    window,
    text="Generate Password",
    bg = "green",
    fg = "white",
    command = handle_click).pack()

window.mainloop()