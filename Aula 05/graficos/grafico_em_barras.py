import matplotlib.pyplot as plt

labels  = ['a','b','c','d','e','f','g']
frequencia = [1,56,56,15,9,99,10]
frequencia.sort()

plt.bar(labels,frequencia)
plt.grid(True)

plt.show()