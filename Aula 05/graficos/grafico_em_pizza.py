import matplotlib.pyplot as plt
import numpy as np

labels  = ['a','b','c','d','e','f','g']
frequencia = [1,56,56,15,9,99,10]
frequencia.sort()

plt.pie(frequencia,labels=labels,autopct='%1.1f%%')
plt.grid(True)

plt.show()