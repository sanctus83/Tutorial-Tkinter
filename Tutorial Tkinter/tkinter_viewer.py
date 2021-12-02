#   visualizador de imagens

from tkinter import *
from PIL import ImageTk,Image

#   criar janela base, dar titulo e definir icone
janelabase = Tk()
janelabase.title("Visualizador Imagens")
janelabase.iconbitmap("icones/fingerprint.ico")

#   definir botoes de accao
botao_sair = Button(janelabase, text="Sair Programa", command=janelabase.quit)
botao_sair.grid(row=0, column=0, columnspan=1)

#   definir qual a imagem a carregar, indicando o caminho
imagem = ImageTk.PhotoImage(Image.open("imagens/img1.jpg"))
#   carregar imagem para o visualizador (como 'Label')
visualizador = Label(image=imagem)
visualizador.grid(row=1, column=0, columnspan=1)

#   chamada para janela principal
janelabase.mainloop()