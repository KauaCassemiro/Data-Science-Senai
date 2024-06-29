import tkinter as tk
from tkinter import ttk


def soma():
    n1 = float(input_enrty.get())
    n2 = float(input_enrty2.get())
    soma = n1 + n2
    label_resultado.config(text=soma)


janela = tk.Tk()
janela.geometry('500x200')
janela.title('Testando tkInter')

text_label = tk.Label(janela,text='Calculadora')
text_label.pack()

input_enrty = tk.Entry(janela)
input_enrty.pack()
input_enrty2 = tk.Entry(janela)
input_enrty2.pack()

botão = tk.Button(janela, text='ok', command=soma)
botão.pack()

label_resultado = tk.Label(janela, text='resultado')
label_resultado.pack()


janela.mainloop()