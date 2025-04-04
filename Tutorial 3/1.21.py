import tkinter as tk

def convert():
    result.set(entry.get().upper())

root = tk.Tk()
root.title("Uppercase Converter")

entry = tk.Entry(root)
entry.pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

tk.Button(root, text="Convert", command=convert).pack()

root.mainloop()
