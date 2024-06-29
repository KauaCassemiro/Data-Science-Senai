import matplotlib.pyplot as plt
import statistics


def moda1(lista):
    moda = statistics.mode(lista)
    print('Moda: ', moda)

def mediana1(lista):
    mediana = statistics.median(lista)
    print('Mediana: ', mediana)

def varianca1(lista):
    varianca = statistics.variance(lista)
    print('Variança: ', varianca)

def desvio1(lista):
    desvio = statistics.stdev(lista)
    print(f'Desvio padrão:  {desvio:.2f}')

def media1(lista):
    media = statistics.mean(lista)
    print('Media: ', media)
 

empresa1 = [1000,6000,1200,8000,1400]
empresa1.sort()
empresa2 = [5000,4000,3000,2000,7000]
empresa2.sort()
empresa3 = [1200,1300,8000,3000,15000]
empresa3.sort()
empresa4 = [1400,1750,2000,4500,5900]
empresa4.sort()

cargos = ['estagiario','assistente','analista','gestor','diretor']

plt.plot(cargos,empresa1, marker = "o")
plt.plot(cargos,empresa2, marker = "o")
plt.plot(cargos,empresa3, marker = "o")
plt.plot(cargos,empresa4, marker = "o")


plt.title('Comparação de Salarios')
plt.ylabel('Faixa salarial')
plt.xlabel('cargos')
plt.grid()

def handle(lista, salarios):

    print('EMPRESA', salarios)
    print('----------------------------')
    media1(lista)
    mediana1(lista)
    moda1(lista)
    varianca1(lista)
    desvio1(lista)


handle(empresa1, empresa1)  
handle(empresa2, empresa2)   
handle(empresa3, empresa3) 
handle(empresa4, empresa4)

plt.show()
enter=input('enter para sair')