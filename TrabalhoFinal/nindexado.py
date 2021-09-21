otimizado_plannig_time = [0.261, 0.197, 0.223, 0.198, 0.195]
otimizado_execution_time = [85.142, 83.217, 84.240, 80.167, 84.782]
notimizado_plannig_time = [0.272, 0.307, 0.250, 0.286, 0.142]
notimizado_execution_time = [85.103, 80.014, 78.872, 83.641, 78.642]

vet = notimizado_execution_time
med = (vet[0] + vet[1] + vet[2] + vet[3] + vet[4]) / 5
print("Média:", round(med, 3))
desvio = ((((vet[0] - med)**2) + ((vet[1] - med)**2) + ((vet[2] - med)**2) + ((vet[3] - med)**2) + ((vet[4] - med)**2)) / 5) ** 0.5
print("Desvio padrão:",round(desvio, 3))