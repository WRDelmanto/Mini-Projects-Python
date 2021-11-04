from tkinter import *

#cria a janela
janela = Tk()

# titulo para a janela
janela.title("Algoritmos")

#configura o tamanho da janela
janela.geometry('500x200')


rotulo = Label(janela, text="Entre com o primeiro número:", font=("Arial Bold", 14))
rotulo.place(x=150, y=20, anchor=CENTER)

rotulo2 = Label(janela, text=" Entre com o segundo número:", font=("Arial Bold", 14))
rotulo2.place(x=150, y=50, anchor=CENTER)

rotulo3 = Label(janela, text="Resultado:", font=("Arial Bold", 14))
rotulo3.place(x=230, y=80, anchor=CENTER)


#cria o elemento de entrada de texto, configura o tamanho
entrada = Entry(janela, width=14, font=("Arial Bold", 14))
entrada.place(x=400, y=20, anchor=CENTER)

#cria o elemento de entrada de texto, configura o tamanho
entrada2 = Entry(janela, width=14, font=("Arial Bold", 14))
entrada2.place(x=400, y=50, anchor=CENTER)

#cria o elemento de entrada de texto, configura o tamanho
entrada3 = Entry(janela, width=14, font=("Arial Bold", 14))
entrada3.place(x=400, y=80, anchor=CENTER)

#definição da função clique
def soma():
    valor1 = entrada.get()
    valor2 = entrada2.get()
    resultado = int(valor1) + int(valor2)
    entrada3.insert(0, resultado)

#cria o botão na janela desejada, com o texto desejado e estabelece
#qual a função que será chamada no clique
btn = Button(janela, text="Soma!", command=soma)

btn.place(x=200, y=120, anchor=CENTER)

#loop infinito para manter a janela aberta
janela.mainloop()