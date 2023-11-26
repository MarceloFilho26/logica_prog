valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))

while valor1 == valor2:
    valor2 = int(input("Números iguais. Digite novamente o segundo número: "))
if valor1 < valor2:
    print(valor1, valor2)
else:
    print(valor2, valor1)
