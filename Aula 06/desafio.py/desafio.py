import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

df = pd.read_csv('C:/Users/aluno/Downloads/Aula 06/desafio.py/dados.csv')

vendas = df['vendas'].values
vendedor = df['vendedor'].values

mean_vendas = np.mean(vendas)
max_vendas = np.max(vendas)
min_vendas = np.min(vendas)

def plot_grafico_barras():
    plt.figure(figsize=(8, 5))
    plt.bar(vendedor, vendas, color='skyblue')
    plt.xlabel('Vendedor')
    plt.ylabel('Vendas')
    plt.title('Vendas por Vendedor')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_grafico_pizza():
    plt.figure(figsize=(6, 6))
    plt.pie(vendas, labels=vendedor, autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição de Vendas')
    plt.axis('equal')
    plt.show()

def plot_grafico_linha():
    plt.figure(figsize=(8, 5))
    plt.plot(vendedor, vendas, marker='o', linestyle='-', color='g', label='Vendas')
    plt.xlabel('Vendedor')
    plt.ylabel('Vendas')
    plt.title('Vendas por Vendedor')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def exibir_estatisticas():
    stats_label['text'] = f'Estatísticas:\nMédia de Vendas: {mean_vendas}\nMáximo de Vendas: {max_vendas}\nMínimo de Vendas: {min_vendas}'

root = Tk()
root.title('Sistema de Análise de Vendas')

btn_barras = Button(root, text='Gráfico de Barras', command=plot_grafico_barras)
btn_barras.pack(pady=10)

btn_pizza = Button(root, text='Gráfico de Pizza', command=plot_grafico_pizza)
btn_pizza.pack(pady=10)

btn_linha = Button(root, text='Gráfico de Linha', command=plot_grafico_linha)
btn_linha.pack(pady=10)

btn_estatisticas = Button(root, text='Exibir Estatísticas', command=exibir_estatisticas)
btn_estatisticas.pack(pady=10)

stats_label = Label(root, text='')
stats_label.pack(pady=10)

root.mainloop()
