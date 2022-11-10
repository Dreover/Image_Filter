from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Apply a filter to an image!")

#Image Containter
content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=550, height=350)
content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))

#buttons
browse_btn = ttk.Button(content, text="Browse")
apply_btn = ttk.Button(content, text="Apply")


#populate listbox
choices = [1, 2, 3, 4, 5]
choice_var = StringVar(value=choices)
fil_list = Listbox(content, listvariable=choice_var, height=5)

#layout config
browse_btn.grid(column=3, row=3, padx=10)
apply_btn.grid(column=4, row=3)
fil_list.grid(column=3, row=1, padx=30)
fil_list.config(height=15, width=25)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)




root.mainloop()