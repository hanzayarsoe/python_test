import tkinter as tk
from PIL import Image, ImageTk

image1 = Image.open("images/nature.jpg")
image1 = image1.resize((500,500))

root = tk.Tk()
img = ImageTk.PhotoImage(image1)
label = tk.Label(root, image=img)
label.pack()

root.mainloop()