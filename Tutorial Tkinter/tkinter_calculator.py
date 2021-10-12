#   calculadora básica em tkinter
#
#   v.01    -   usar funcoes lambda como comando nos metodos 'Button()' para evitar duplicação de código
#   v.02    -   separar os metodos usados nos comandos dos botoes, em vez de usar um metodo unico e processar os codigos dos botoes

from tkinter import *

#   variavel para guardar valor temporario entre operacoes aritmeticas
memoria = 0.00

#   variavel booleana para identificar que estamos dentro de uma operacao aritmetica
operacao = False

#   definir as funções matemáticas básicas
def somar(num1: float, num2: float):
    return num1 + num2

def subtrair(num1: float, num2: float):
    return num1 - num2

def dividir(num1: float, num2: float):
    return num1 / num2

def multiplicar(num1: float, num2: float):
    return num1 * num2

#   criar janela principal
janelabase = Tk()
janelabase.title("Basic Calc")

#   criar mostrador
mostrador = Entry(janelabase, width=45, border=5, justify=RIGHT)
mostrador.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
mostrador.insert(0, "0")

#   definir accao de botoes com base no codigo de accao
def accaoBotao(codigo: int):
    global memoria
    global operacao
    msg = mostrador.get()   #   criar copia do conteudo do mostrador...
    mostrador.delete(0,END) #   ... e limpar mostrador
    #   processar codigo de botoes de digitos ou virgula
    if (codigo < 11):
        if (msg == "0" or operacao):  #   se no mostrador estiver apenas "0" ou estivermos a meio de uma operacao aritmetica, apagar o mostrador e colocar o que foi digitado
            msg = ""
            operacao ^= operacao    #   limpar flag operacao caso seja True
        if (codigo == 10):  #   se for pressionado o botao de virgula, verificar se já existe virgula no mostrador
            if (msg.count(',') == 0):   #   processar se não existir...
                codigo = ","
            else:
                mostrador.insert(0, msg)    #   ... nao processar e manter mostrador igual
                return
        msg = msg + str(codigo)
    #   processar codigo de botao de limpar
    if (codigo == 13):
        msg = "0"               #   passar '0' no mostrador
        operacao ^= operacao    #   colocar a False a flag operacao
        memoria = 0.00          #   limpar a variavel global de memoria
    #   processar codigo de botao de somar
    if (codigo == 12):
        msg = str(somar(memoria, float(msg.replace(',','.'))))
        memoria = float(msg.replace(',','.'))
        operacao = True
    #   processar codigo de botao de dividir
    if (codigo == 14):
        msg = str(dividir(memoria, float(msg.replace(',','.'))))
        memoria = float(msg.replace(',','.'))
        operacao = True
    #   processsar codigo de botao de multiplicar
    if (codigo == 15):
        msg = str(multiplicar(memoria, float(msg.replace(',','.'))))
        memoria = float(msg.replace(',','.'))
        operacao = True
    #   processar codigo de botao de subtrair
    if (codigo == 16):
        msg = str(subtrair(float(msg.replace(',','.')), memoria))
        memoria = float(msg.replace(',','.'))
        operacao = True
    #   mostrar resultado
    if (codigo == 11):
        operacao ^= operacao
        msg = str(memoria)
    mostrador.insert(0, msg.replace('.',','))

#   criar botões da calculadora
bLargura = 9   #   macro para largura de butoes
bAltura = 3    #   macro para altura de butoes

#   botoes para digitos e virgula
bNum1 = Button(janelabase, text="1", width=bLargura, height=bAltura, command=lambda: accaoBotao(1))
bNum1.grid(row=4, column=0)
bNum2 = Button(janelabase, text="2", width=bLargura, height=bAltura, command=lambda: accaoBotao(2))
bNum2.grid(row=4, column=1)
bNum3 = Button(janelabase, text="3", width=bLargura, height=bAltura, command=lambda: accaoBotao(3))
bNum3.grid(row=4, column=2)
bNum4 = Button(janelabase, text="4", width=bLargura, height=bAltura, command=lambda: accaoBotao(4))
bNum4.grid(row=3, column=0)
bNum5 = Button(janelabase, text="5", width=bLargura, height=bAltura, command=lambda: accaoBotao(5))
bNum5.grid(row=3, column=1)
bNum6 = Button(janelabase, text="6", width=bLargura, height=bAltura, command=lambda: accaoBotao(6))
bNum6.grid(row=3, column=2)
bNum7 = Button(janelabase, text="7", width=bLargura, height=bAltura, command=lambda: accaoBotao(7))
bNum7.grid(row=2, column=0)
bNum8 = Button(janelabase, text="8", width=bLargura, height=bAltura, command=lambda: accaoBotao(8))
bNum8.grid(row=2, column=1)
bNum9 = Button(janelabase, text="9", width=bLargura, height=bAltura, command=lambda: accaoBotao(9))
bNum9.grid(row=2, column=2)
bNum0 = Button(janelabase, text="0", width=(bLargura*2)+1, height=bAltura, command=lambda: accaoBotao(0))
bNum0.grid(row=5, column=0, columnspan=2)
bVirgula = Button(janelabase, text=",", width=bLargura, height=bAltura, command=lambda: accaoBotao(10))
bVirgula.grid(row=5, column=2)

#   botoes para operações aritmeticas
bResultado = Button(janelabase, text="=", width=bLargura, height=(bAltura*2)+1, command=lambda: accaoBotao(11))
bResultado.grid(row=4, column=3, rowspan=2)
bSomar = Button(janelabase, text="+", width=bLargura, height=(bAltura*2)+1, command=lambda: accaoBotao(12))
bSomar.grid(row=2, column=3, rowspan=2)
bLimpar = Button(janelabase, text="Limpar", width=bLargura, height=bAltura, command=lambda: accaoBotao(13))
bLimpar.grid(row=1, column=0)
bDividir = Button(janelabase, text="/", width=bLargura, height=bAltura, command=lambda: accaoBotao(14))
bDividir.grid(row=1, column=1)
bMultiplicar = Button(janelabase, text="*", width=bLargura, height=bAltura, command=lambda: accaoBotao(15))
bMultiplicar.grid(row=1, column=2)
bSubtrair = Button(janelabase, text="-", width=bLargura, height=bAltura, command=lambda: accaoBotao(16))
bSubtrair.grid(row=1, column=3)

janelabase.mainloop()