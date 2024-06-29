import matplotlib.pyplot as plt

ano = [2021,2022,2023,2024,2025,2026]
vendas = [10000,2000,30000,10000,5000,20000]

plt.title('Vendas por Ano')
plt.plot(ano,vendas, marker = 'o')
plt.xlabel('ano')
plt.ylabel('vendas')
plt.grid()

plt.show()

medias_jose = [10,5,8,9,10,5,4]
meses = ['fev','mar', 'abril', 'maio', 'junho', 'julho', 'agosto']
plt.bar(meses,medias_jose)
plt.grid()



plt.show()