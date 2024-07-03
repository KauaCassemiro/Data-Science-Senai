from matplotlib import pyplot as plt
from  media import media1
from mediana import mediana1
from variancia import varianca1
from desvio import desvio1
from moda import moda1


empresa1 = [1000,6000,1200,8000,1400]
empresa1.sort()
empresa2 = [5000,4000,3000,2000,7000]
empresa2.sort()
empresa3 = [1200,1300,8000,3000,15000]
empresa3.sort()
empresa4 = [1400,1750,2000,4500,5900,]
empresa4.sort()

cargos = ['estagiario', 'tecnico', 'assistente', 'analista', 'gerente']

def hadle(lista, salarios):

    print('\n----------------------------')
    print('EMPRESA', salarios)
    media1(lista)
    mediana1(lista)
    moda1(lista)
    varianca1(lista)
    desvio1(lista)


hadle(empresa1, empresa1)  
hadle(empresa2, empresa2)   
hadle(empresa3, empresa3) 
hadle(empresa4, empresa4)

plt.plot(cargos,empresa1)

plt.show()