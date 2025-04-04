import tkinter as tk
from tkinter import messagebox
import math

def compute_sqrt():
    try:
        num = float(entry.get())
        result.set(round(math.sqrt(num), 2))
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Enter a number.")

root = tk.Tk()
root.title("Square Root Calculator")

entry = tk.Entry(root)
entry.pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

tk.Button(root, text="Compute", command=compute_sqrt).pack()

root.mainloop()
