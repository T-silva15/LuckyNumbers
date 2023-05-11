from tkinter import *
import tkinter.font as font
from PIL import Image
import random

#window configuration
window = Tk()
window.title("Lucky Numbers") 
window.iconbitmap('LuckyNumbers\imageFiles\icon.ico')
window.configure(bg='#8beae9')
window.geometry('1000x600')

#function that clears screen
def clearScreen(window):
    for widgets in window.winfo_children():
      widgets.destroy()

#function that clears screen and shows a brief description of the game
def showDescription():
    clearScreen(window)
    desc = Label(window, text='O Lucky Numbers é um jogo de tabuleiro no qual o jogador precisa de formar uma sequência crescente\n de números, tanto na horizontal quanto na vertical. A cada jogada é fornecido um novo número, exceto\n quando o jogador não coloca o número atribuído na jogada anterior ou troca com um número já presente\n no tabuleiro. Quando isso acontece, o número substituído é colocado em uma mesa separada, que\n ambos os jogadores têm acesso e podem utilizar para futuras trocas, caso seja conveniente.', font=("arial", 12), bg='#56ace8', bd = 25, highlightthickness = 3, highlightbackground = '#363434')
    desc.place(x = 100, y = 100)
    button_back= Button(window, text='Voltar ao Menu', font=("arial", 10), bg='#56ace8', command=gameMenu)
    button_back.place(x = 425, y = 300)

#fucntion that puts game menu on screen
def gameMenu():
    clearScreen(window)
    #text creation 
    text_menu = Label(window, text='MENU', font=("04b", 40, font.BOLD), bg='#56ace8', bd = 7, highlightthickness = 3, highlightbackground = '#363434')
    text_menu.place(x=350, y=100)
    text_A = Label(window, text='Jogar uma Partida', font=("arial", 10), bg='#8beae9')
    text_A.place(x=375, y=215)
    text_B = Label(window, text='Carregar uma partida a partir de um ficheiro', font=("arial", 10), bg='#8beae9')
    text_B.place(x=375, y=245)
    text_C = Label(window, text='Descrição do jogo', font=("arial", 10), bg='#8beae9')
    text_C.place(x=375, y=275)
    text_D = Label(window, text='Sair da aplicação', font=("arial", 10), bg='#8beae9')
    text_D.place(x=375, y=305)

    #button creation
    button_A = Button(window, text='A', font=("arial", 10), bg='#56ace8', command=exit)
    button_A.place(x=350, y=210)
    button_B = Button(window,text='B', font=("arial", 10), bg='#56ace8', command=exit)
    button_B.place(x=350, y=240)
    button_C = Button(window, text='C', font=("arial", 10), bg='#56ace8', command=showDescription)
    button_C.place(x=350, y=270)
    button_D = Button(window, text='D', font=("arial", 10), bg='#56ace8', command=exit)
    button_D.place(x=350, y=300)

#calls menu function
gameMenu()
#runs tkloop (listens to events)
window.mainloop()