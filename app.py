from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image

def upload():
    global img
    f_types = [("PNG Files", "*.png"), ("All Files", "*.*"),
               ("Jpg Files", "*.jpg")]
    img_path = filedialog.askopenfilename(title="Select an Image",
                                          filetypes=f_types)
    img_size = (300, 250)  
    img = ImageTk.PhotoImage(Image.open(img_path).resize(img_size)) 
    place_img = ttk.Label(frame, image=img)
    place_img.grid(column=0, row=0)
    
def get_filter():
    pass
    
root = Tk()
root.title("Apply a filter to an image!")

#Image Containter
content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, width=550, height=350)
content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))

#Buttons
apply_btn = ttk.Button(content, text="Apply")
save_btn = ttk.Button(content, text="Save")
upload_btn = ttk.Button(content, text="Upload", command=upload)

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
upload_btn.grid(column=4, row=0)
upload_btn.config(width=10)

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