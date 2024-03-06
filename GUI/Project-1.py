# Problem 2
#Title: Simple Counter Application with Tkinter 
#Problem Statement: Design and implement a simple counter application using Tkinter, a Python GUI library.
#                   The application should provide users with a graphical user interface featuring a counter label 
#                   and two buttons for incrementing and decrementing the counter value. 
from tkinter import *
import sys
import random
root = Tk()
root.geometry(f"450x450")
var = "Push me Harder"
root.count = 1
def button_click():
    label.config(text="You clicked the button")
    root.count += 1
    # var = "Push Me Harder"
    label['text'] = (root.count)
    if root.count <10:
        label.config(font=('Ariel',50), fg="green")
    else:
        label.config(font=('Ariel',50), fg="red")

def button_click2():
    label.config(text="You clicked the button")
    
    root.count -= 1
    if root.count >0:
        label['text'] = (root.count)
    else:
        root.count = 0

    if root.count <10:
        label.config(font=('Ariel',50), fg="green")
    else:
        label.config(font=('Ariel',50), fg="red")        



label = Label(root, text="Nameste Duniya")
label.pack()

button = Button(root, text="PUSH ME ABOVE", command=button_click)
button.pack(side=LEFT, ipadx=20, ipady=20, padx=10, pady=10)

button2 = Button(root, text="PUSH ME DOWN", command=button_click2)
button2.pack(side=RIGHT, ipadx=20, ipady=20, padx=10, pady=10)

button3 = Button(root, text="EXIT", command=sys.exit)
button3.pack(side=RIGHT, ipadx=20, ipady=20, padx=10, pady=10)
root.mainloop()