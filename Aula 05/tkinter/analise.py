import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import statistics
from tkinter import messagebox
from matplotlib.figure import Figure

def calcular_estatistica(lista):
    media = statistics.mean(lista)
    moda = statistics.mode(lista)
    mediana = statistics.median(lista)
    desvio = statistics.stdev(lista)
    varianca = statistics.variance(lista)
    return media , mediana, moda ,desvio, varianca

def mostrar_analise():
    empresa1 = [1000,6000,1200,8000,1400]
    empresa1.sort()
    empresa2 = [5000,4000,3000,2000,7000]
    empresa2.sort()
    empresa3 = [1200,1300,8000,3000,15000]
    empresa3.sort()
    empresa4 = [1400,1750,2000,4500,5900]
    empresa4.sort()

    empresa_selecionada = empresa_var.get()
    if empresa_selecionada == 'Empresa 1':
        dados = empresa1
    elif empresa_selecionada == 'Empresa 2':
        dados = empresa2
    elif empresa_selecionada == 'Empresa 3':
        dados = empresa3
    elif empresa_selecionada == 'Empresa 4':
        dados = empresa4
    else:
        messagebox.showerror('Erro - Não há dados sobre essa empresa')
        return
    
    media, moda, mediana, desvio, varianca = calcular_estatistica(dados)



    cargos = ['Estagiario', 'Vendedor', 'Supervisor', 'Gestor', 'CEO']

    resultado_text = (f''''
                        Média {media}
                        Moda {moda}
                        Mediana {mediana}
                        Desvio de padrão {desvio}
                        Variança {varianca}
                      ''')
    resultado_label.config(text = resultado_text)

    fig = Figure(figsize =(6,4), dpi = 100)
    ax = fig.add_subplot(111)
    ax.set_title('cargos e salarios')
    ax.set_xlabel('cargos')
    ax.set_ylabel('salarios')
    ax.plot(cargos, dados)
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

root = tk.Tk()
root.title('Cargos e salarios')
empresa_var = tk.StringVar(value='Empresa 1')
empresa_opcoes = ['Empresa 1', 'Empresa 2', 'Empresa 3', 'Empresa 4']
menu = ttk.Combobox(root,textvariable = empresa_var, values = empresa_opcoes)
menu.pack()

btn= tk.Button(root, text='Analise', command=mostrar_analise)
btn.pack()

resultado_label = tk.Label(root, text='')
resultado_label.pack(pady=10)



root.mainloop()