import tkinter as tk

root = tk.Tk()
root.title("Button widget")

tk.Button(root,text="Click Me!",relief="raised").pack()
tk.Button(root,text="Click Me!",relief="sunken").pack()
tk.Button(root,text="Click Me!",relief="flat").pack()
tk.Button(root,text="Click Me!",relief="ridge").pack()
tk.Button(root,text="Click Me!",relief="groove").pack()
tk.Button(root,text="Click Me!",relief="solid").pack()
root.mainloop()