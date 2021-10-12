from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="butao clicado!")
    myLabel.pack()

myButton = Button(root, text="Carrega aqui!", command=myClick, bg="purple")
myButton.pack()

root.mainloop()