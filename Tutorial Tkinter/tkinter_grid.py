from tkinter import *

root = Tk()

# criar etiqueta
myLabel1 = Label(root, text="Olá Mundo!")
myLabel2 = Label(root, text="tkinter")

# por em grelhas e enviar para o ecra
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)

# correr mainloop
root.mainloop()
