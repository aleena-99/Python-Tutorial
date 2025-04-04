import tkinter as tk

def calculate_distance():
    h = float(entry_h.get())
    b = float(entry_b.get())
    n = int(entry_n.get())
    
    total_distance = 0
    for _ in range(n):
        total_distance += h
        h *= b
        total_distance += h

    result.set(f"Total Distance: {round(total_distance, 2)}")

root = tk.Tk()
root.title("Bouncy Ball Distance")

tk.Label(root, text="Initial Height").pack()
entry_h = tk.Entry(root)
entry_h.pack()

tk.Label(root, text="Bounciness Index").pack()
entry_b = tk.Entry(root)
entry_b.pack()

tk.Label(root, text="Number of Bounces").pack()
entry_n = tk.Entry(root)
entry_n.pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

tk.Button(root, text="Calculate", command=calculate_distance).pack()

root.mainloop()
