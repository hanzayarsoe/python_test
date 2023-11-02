import tkinter as tk

root = tk.Tk()
root.title("Entry Widget")

label = tk.Label(root, text="Name: ")
entry = tk.Entry(root)

entry.insert(0,"Enter your name")
entry.config(state="disabled")

label.pack()
entry.pack()

root.mainloop()