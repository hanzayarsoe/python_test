import tkinter as tk

root = tk.Tk()
root.title("label testing")

label = tk.Label(root, text="label in Tkinter",bg="lightgreen", font="arial",padx=20,pady=50)

label.pack()

root.mainloop()