from tkinter import *
from PIL import ImageTk,Image

janelabase = Tk()
janelabase.title("radiobutton")
janelabase.iconbitmap("./icones/fingerprint.ico")

# r = IntVar()
# r.set("2")

MODOS = [
    ("Chouriço", "Chouriço"),
    ("Queijo", "Queijo"),
    ("Cogumelos", "Cogumelos"),
    ("Cebola", "Cebola")
    ]

pizza = StringVar()
pizza.set("Chouriço")

for texto, modo in MODOS:
    Radiobutton(janelabase, text=texto, variable=pizza, value=modo).pack(anchor=W)

def click(valor):
    etiqueta = Label(janelabase, text=valor).pack()

# Radiobutton(janelabase, text="Opção 1", variable=r, value=1, command=lambda: click(r.get())).pack()
# Radiobutton(janelabase, text="Opção 2", variable=r, value=2, command=lambda: click(r.get())).pack()

# etiqueta = Label(janelabase, text=r.get()).pack()

janelabase.mainloop()
