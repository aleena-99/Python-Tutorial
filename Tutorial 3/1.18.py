import random
import tkinter as tk

low, high = 1, 100
guess = random.randint(low, high)

def too_large():
    global high, guess
    high = guess - 1
    guess_again()

def too_small():
    global low, guess
    low = guess + 1
    guess_again()

def correct():
    label.config(text=f"Yay! The correct number is {guess}")

def guess_again():
    global guess
    if low <= high:
        guess = random.randint(low, high)
        label.config(text=f"Is it {guess}?")
    else:
        label.config(text="Something went wrong!")

root = tk.Tk()
root.title("Computer Guesses")

label = tk.Label(root, text=f"Is it {guess}?")
label.pack()

tk.Button(root, text="Too Large", command=too_large).pack()
tk.Button(root, text="Too Small", command=too_small).pack()
tk.Button(root, text="Correct", command=correct).pack()

root.mainloop()
