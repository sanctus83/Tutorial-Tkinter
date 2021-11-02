#   calculadora básica em tkinter
#   
#   luis rodrigues 2021
#   sanctus.hck@gmail.com
#
#   v.01    -   usar funcoes lambda como comando nos metodos 'Button()' para evitar duplicação de código
#   v.02    -   separar os metodos usados nos comandos dos botoes, em vez de usar um metodo unico e processar os codigos dos botoes


from tkinter import *

#   variavel para guardar valor temporario entre operacoes aritmeticas
memoria = 0.00

#   variavel que guarda o código da operação aritmética a ser realizada
#   0 = nenhuma operação
#   1 = soma
#   2 = subtração
#   3 = multiplicação
#   4 = divisão
operacao = 0

#   variavel para indicar se valor no mostrador é resultado final. usado para ignorar o valor do mostrador (e assim limpar) quando iniciamos outra accao
resultado = True

#   criar janela principal
janelabase = Tk()
janelabase.title("Calculadora Básica")

#   criar mostrador
mostrador = Entry(janelabase, width=45, border=5, justify=RIGHT)
mostrador.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
mostrador.insert(0, "0,0")

#   definir accao dos botoes de digitos e virgula
def accaoDigito(codigo):
    global operacao
    global resultado
    msg = mostrador.get()       #   criar copia do conteudo do mostrador
    mostrador.delete(0, END)    #   apagar conteudo no mostrador
    #   processar codigos de botoes de digito ou virgula
    if (codigo < 11):
        if (resultado or operacao):     #   se mostrador contém resultado final da ultima operação ou se estivermos a meio de uma operacao
            msg = ""                    #   apagar conteudo do mostrador e colocar o que foi digitado
            resultado = False           #   indicar que o está no mostrador não é resultado final
        if (codigo == 10):              #   se for pressionada a virgula...
            if (msg.count(',') == 0):   #   ... verificar se não existe virgula ainda
                codigo = ','
            else:                               #   ignorar se já existir
                mostrador.insert(0, msg)   
                return
        msg = msg + str(codigo)                 #   adicionar digito/virgula ao conteudo existente no mostrador
    mostrador.insert(0, msg.replace('.',','))   #   actualizar mostrador com novo conteudo (para ficar mais bonito, substitui-se '.' por ',')

#   definir accao do botao 'Limpar' (queremos limpar só mostrador, ou limpar também flag 'operacao' e 'memoria'?)
def accaoLimpar():
    global operacao
    global memoria
    global resultado
    operacao = 0
    memoria = 0.00
    resultado = True
    mostrador.delete(0, END)
    mostrador.insert(0, '0,0')
    return

#   definir accao do botao 'Somar'
def accaoSomar(valor):
    global operacao
    global memoria
    global resultado
    valor = float(str(valor).replace(',','.'))
    if operacao != 0:               #   se estiver em curso uma operação, realizar operação
        accaoResultado(float(valor))
    else:                           #   caso contrário, executa a soma de 'memoria' com 'valor'
        memoria += float(valor)
    operacao = 1                    #   assinalar operação soma
    resultado = False               #   indicar que o está no mostrador não é resultado final
    return

#   definir accao do botao 'Subtrair'
def accaoSubtrair(valor):
    global operacao
    global memoria
    global resultado
    valor = float(str(valor).replace(',','.'))
    if operacao != 0:               #   se estiver em curso uma operação, realizar operação
        accaoResultado(float(valor))
    else:                           #   caso contrário, executa a subtracao de 'memoria' com 'valor'
        memoria = float(valor) - memoria
    operacao = 2                    #   assinalar operação subtração
    resultado = False               #   indicar que o está no mostrador não é resultado final
    return

#   definir accao do botao 'Multiplicar'
def accaoMultiplicar(valor):
    global operacao
    global memoria
    global resultado
    valor = float(str(valor).replace(',','.'))
    if operacao != 0:               #   se estiver em curso uma operação, realizar operação
        accaoResultado(float(valor))
    else:                           #   caso contrário, executa a multiplicacao de 'memoria' com 'valor'
        memoria = float(valor) if memoria == 0 else float(valor) * memoria
    operacao = 3                    #   assinalar operação multiplicação
    resultado = False               #   indicar que o está no mostrador não é resultado final
    return

#   definir accao do botao 'Divisao'
def accaoDividir(valor):
    global operacao
    global memoria
    global resultado
    valor = float(str(valor).replace(',','.'))
    if operacao != 0:               #   se estiver em curso uma operação, realizar operação
        accaoResultado(float(valor))
    else:                           #   caso contrário, executa a divisao de 'memoria' com 'valor'       
        memoria = float(valor) if memoria == 0 else memoria / float(valor)
    operacao = 4                    #   assinalar operação divisão
    resultado = False               #   indicar que o está no mostrador não é resultado final
    return

#   definir accao do botao 'Resultado'
def accaoResultado(valor):
    global operacao
    global memoria
    global resultado
    valor = float(str(valor).replace(',','.'))
    #   realizar a operação aritmética com código 'operacao' entre valor guardado em 'memoria' e 'valor'
    if operacao == 1:
        memoria += float(valor)
    elif operacao == 2:
        memoria -= float(valor)
    elif operacao == 3:
        memoria *= float(valor)
    elif operacao == 4:
         memoria /= float(valor)
    mostrador.delete(0, END)                            #   limpar mostrador
    mostrador.insert(0, str(memoria).replace('.',','))  #   colocar no mostrador o resultado
    operacao = 0                                        #   assinalar nenhuma operação
    memoria = 0.0                                       #   limpar memoria
    resultado = True                                    #   indicar que foi mostrado resultado final
    return

#   criar botões da calculadora
bLargura = 9   #   macro para largura de butoes
bAltura = 3    #   macro para altura de butoes

#   botoes para digitos e virgula
bNum1 = Button(janelabase, text="1", width=bLargura, height=bAltura, command=lambda: accaoDigito(1))
bNum1.grid(row=4, column=0)
bNum2 = Button(janelabase, text="2", width=bLargura, height=bAltura, command=lambda: accaoDigito(2))
bNum2.grid(row=4, column=1)
bNum3 = Button(janelabase, text="3", width=bLargura, height=bAltura, command=lambda: accaoDigito(3))
bNum3.grid(row=4, column=2)
bNum4 = Button(janelabase, text="4", width=bLargura, height=bAltura, command=lambda: accaoDigito(4))
bNum4.grid(row=3, column=0)
bNum5 = Button(janelabase, text="5", width=bLargura, height=bAltura, command=lambda: accaoDigito(5))
bNum5.grid(row=3, column=1)
bNum6 = Button(janelabase, text="6", width=bLargura, height=bAltura, command=lambda: accaoDigito(6))
bNum6.grid(row=3, column=2)
bNum7 = Button(janelabase, text="7", width=bLargura, height=bAltura, command=lambda: accaoDigito(7))
bNum7.grid(row=2, column=0)
bNum8 = Button(janelabase, text="8", width=bLargura, height=bAltura, command=lambda: accaoDigito(8))
bNum8.grid(row=2, column=1)
bNum9 = Button(janelabase, text="9", width=bLargura, height=bAltura, command=lambda: accaoDigito(9))
bNum9.grid(row=2, column=2)
bNum0 = Button(janelabase, text="0", width=(bLargura*2)+1, height=bAltura, command=lambda: accaoDigito(0))
bNum0.grid(row=5, column=0, columnspan=2)
bVirgula = Button(janelabase, text=",", width=bLargura, height=bAltura, command=lambda: accaoDigito(10))
bVirgula.grid(row=5, column=2)

#   botoes para operações aritmeticas
bResultado = Button(janelabase, text="=", width=bLargura, height=(bAltura*2)+1, command=lambda: accaoResultado(mostrador.get()))
bResultado.grid(row=4, column=3, rowspan=2)
bSomar = Button(janelabase, text="+", width=bLargura, height=(bAltura*2)+1, command=lambda: accaoSomar(mostrador.get()))
bSomar.grid(row=2, column=3, rowspan=2)
bLimpar = Button(janelabase, text="Limpar", width=bLargura, height=bAltura, command=accaoLimpar)
bLimpar.grid(row=1, column=0)
bDividir = Button(janelabase, text="/", width=bLargura, height=bAltura, command=lambda: accaoDividir(mostrador.get()))
bDividir.grid(row=1, column=1)
bMultiplicar = Button(janelabase, text="*", width=bLargura, height=bAltura, command=lambda: accaoMultiplicar(mostrador.get()))
bMultiplicar.grid(row=1, column=2)
bSubtrair = Button(janelabase, text="-", width=bLargura, height=bAltura, command=lambda: accaoSubtrair(mostrador.get()))
bSubtrair.grid(row=1, column=3)

janelabase.mainloop()