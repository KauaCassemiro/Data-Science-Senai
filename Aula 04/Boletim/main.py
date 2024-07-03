from amplitude import amplitude
from desvio_de_padrao import calcular_desvio_padrao
from media import calcular_media
from mediana import mediana
from moda import calcular_moda
from variancia import calcular_variancia

notas = {
    'ensino medio' : {5, 7, 6, 8, 6, 9, 3, 2, 4},
    'ensino fundamental' : {1, 8, 9, 10, 3, 5, 8, 8, 9}
}

def analise_media(notas):
    for classe, conjunto_notas in notas.items():
        ampli = amplitude(conjunto_notas)
        desvio_padrao = calcular_desvio_padrao(conjunto_notas)
        media = calcular_media(conjunto_notas)
        mediana_valor = mediana(conjunto_notas)
        moda_valor = calcular_moda(conjunto_notas)
        variancia = calcular_variancia(conjunto_notas)       

        print(f"\n------Análise do {classe}------")
        print(f"Amplitude: {ampli}")
        print(f"Desvio Padrão: {desvio_padrao}")
        print(f"Média: {media}")
        print(f"Mediana: {mediana_valor}")
        print(f"Moda: {moda_valor}")
        print(f"Variância: {variancia}")


analise_media(notas)

enter = input('Clique enter para sair')

