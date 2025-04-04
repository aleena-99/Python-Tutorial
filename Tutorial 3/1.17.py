import random
import tkinter as tk
from tkinter import messagebox

target = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    attempts += 1
    guess = int(entry.get())

    if guess > target:
        messagebox.showinfo("Hint", "Too large, try again!")
    elif guess < target:
        messagebox.showinfo("Hint", "Too small, try again!")
    else:
        messagebox.showinfo("Success", f"Correct! Total guesses: {attempts}")

root = tk.Tk()
root.title("Guess the Number")

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Submit", command=check_guess).pack()

root.mainloop()
