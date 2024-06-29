import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# func para graficos
def grafico():

    # dados
    vendas_em_milhoes = [15, 20, 30, 6, 89, 15, 20]
    meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN','JUL']

    # criando grafico
    fig, ax = plt.subplots() 
    ax.pie(vendas_em_milhoes, labels = meses, autopct='%1.1f%%' )

    # rótulos
    # ax.set_xlabel('MESES')
    # ax.set_ylabel('VENDAS')
    ax.set_title('GRÁFICO DE VENDA')
    ax.grid(True)

    # integração do gráfico
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

root = tk.Tk()
root.title('Vendas')

frame_grafico = tk.Frame(root)
frame_grafico.pack()

button = tk.Button(root, text='Mostrar Gráfico', command=grafico)
button.pack(padx=10)




root.mainloop()