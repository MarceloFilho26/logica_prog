notas = [0, 0, 0, 0, 0]
soma = 0
for x in range(5):
    notas[x] = float(input(f"Informe a {x + 1} nota: "))

for y in range(5):
    soma = soma + notas[y]
media = soma / 5

for z in range(5):
    if notas[z] >= media:
        print(notas[z])