otimizado_plannig_time = [0.491, 0.525, 0.255, 0.449, 0.320]
otimizado_execution_time = [92.335, 82.660, 85.518, 86.039, 85.604]
notimizado_plannig_time = [0.464, 0.264, 0.426, 0.568, 0.529]
notimizado_execution_time = [87.202, 82.414, 86.138, 87.340, 83.133]

vet = notimizado_execution_time
med = (vet[0] + vet[1] + vet[2] + vet[3] + vet[4]) / 5
print("Média:", round(med, 3))
desvio = ((((vet[0] - med)**2) + ((vet[1] - med)**2) + ((vet[2] - med)**2) + ((vet[3] - med)**2) + ((vet[4] - med)**2)) / 5) ** 0.5
print("Desvio padrão:",round(desvio, 3))