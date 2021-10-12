from tkinter import *

root = Tk()

data = Entry(root, width=50, bg="red", fg="white", borderwidth=10)
data.pack()
data.insert(0, "introduza o seu nome")

def myClick():
    msg = "Olá " + data.get()
    myLabel = Label(root, text=msg)
    myLabel.pack()

myButton = Button(root, text="Introduza nome:", command=myClick, bg="purple")
myButton.pack()

root.mainloop()