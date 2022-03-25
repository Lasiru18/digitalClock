from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

# set label
label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor="center")
time()

# calling to mainloop
mainloop()