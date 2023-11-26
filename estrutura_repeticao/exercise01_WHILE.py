nota = int(input("Digite uma nota: "))

while (nota < 0) or (nota > 10):
    print("Notas inválidas")
else:
    print("Sucesso!")
