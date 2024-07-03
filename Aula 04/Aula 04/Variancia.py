import statistics

dados = list(range(100,600))
varianc = statistics.variance(dados)
print(varianc)

dados = list(range(100,1000, 2))
varianc = statistics.variance(dados)
print(dados)
print(varianc)