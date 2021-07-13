print("Quastão 1")
print("Com conn.autocommit = False")
vet = [14.80381727218628, 14.087637186050415, 13.7781982421875, 14.281881332397461, 14.440276384353638]
med = (vet[0] + vet[1] + vet[2] + vet[3] + vet[4]) / 5
print("Média:", med)
desvio = ((((vet[0] - med)**2) + ((vet[1] - med)**2) + ((vet[2] - med)**2) + ((vet[3] - med)**2) + ((vet[4] - med)**2)) / 5) ** 0.5
print("Desvio padrão:",desvio)
print("═════════════════════════════════")

print("Com conn.autocommit = True")
vet = [62.52215123176575, 64.21055960655212, 61.676618337631226, 65.82042741775513, 66.98765325546265]
med = (vet[0] + vet[1] + vet[2] + vet[3] + vet[4]) / 5
print("Média:", med)
desvio = ((((vet[0] - med)**2) + ((vet[1] - med)**2) + ((vet[2] - med)**2) + ((vet[3] - med)**2) + ((vet[4] - med)**2)) / 5) ** 0.5
print("Desvio padrão:",desvio)
print("═════════════════════════════════\n\n")