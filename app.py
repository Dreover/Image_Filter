from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image

def browse():
    img_path = filedialog.askopenfilename(title="Select an Image",
                                          filetypes=(("PNG Files", "*.png"),
                                                     ("JPEG Files", "*.jpeg;*.jpg"),
                                                     ("All Files", "*,*")))
    img = Image.open(img_path)
    image_label = ttk.Label(frame, image=img)
root = Tk()
root.title("Apply a filter to an image!")

#Image Containter
content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=550, height=350)
content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))

#Buttons
apply_btn = ttk.Button(content, text="Apply")
save_btn = ttk.Button(content, text="Save")
browse_btn = ttk.Button(content, text="Browse", command=browse)

#Labels
fil_label = ttk.Label(content, text="Select a filter below")

#Populate Listbox
choices = ["Greyscale", "Sharp", "Sepia", "Invert", "Pencil Scetch"]
choice_var = StringVar(value=choices)
fil_list = Listbox(content, listvariable=choice_var, height=5)

#Layout Config
apply_btn.grid(column=3, row=3, padx=10)
apply_btn.config(width=10)
save_btn.grid(column=4, row=3)
save_btn.config(width=10)
fil_list.grid(column=3, row=1, padx=30)
fil_list.config(height=5, width=10)
fil_label.grid(column=3, row=0)
browse_btn.grid(column=4, row=0)
browse_btn.config(width=10)

#Grid Config
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()