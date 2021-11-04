from tkinter import *
import os
import random

Steam_Path = 'Z:\Steam\steamapps\common'

#Cria a janela
janela = Tk()

# Titulo da janela
janela.title("Jogo Aleatório")

#Tamanho da janela
janela.geometry('500x400')


rotulo = Label(janela, text="Jogo de Hoje:", font=("Arial Bold", 20))
rotulo.place(x=250, y=50, anchor=CENTER)

rotulo1 = Label(janela, text='******', width=60, font=("Arial", 10))
rotulo1.place(x=250, y=200, anchor=CENTER)

rotulo2 = Label(janela, text="Caminho da Steam:", font=("Arial Bold", 14))
rotulo2.place(x=100, y=375, anchor=CENTER)


#Entrada de texto do caminho da steam
entrada1 = Entry(janela, width=45, font=("Arial", 8))
entrada1.place(x=325, y=375, anchor=CENTER)
entrada1.insert(0, Steam_Path)


#Função que seleciona o jogo
def select_game():
    steam_path = entrada1.get()
    
    games = []
    
    for entry in os.listdir(steam_path):
        if os.path.isdir(os.path.join(steam_path, entry)):
            games.append(entry)
            
    Random_Number = random.randrange(0, len(games) - 1)
    
    
    rotulo1.config(text = games[Random_Number])


#Cria o botão na janela desejada, com o texto desejado e estabelece qual a função que será chamada no clique
btn = Button(janela, text="Clique Aqui!", command=select_game)
btn.place(x=250, y=300, anchor=CENTER)

#loop infinito para manter a janela aberta
janela.mainloop()