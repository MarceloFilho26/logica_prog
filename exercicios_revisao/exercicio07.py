base = float(input("Informe o valor da base: "))
while base <= 0:
    base = float(input("Número inválido. Informe o valor da base novamente: "))

altura = float(input("Informe o valor da altura: "))
while altura <= 0:
    altura = float(input("Número inválido. Informe o valor da altura novamente: "))

area = (base * altura) / 2
print(f"O valor da área corresponde a {area}.")