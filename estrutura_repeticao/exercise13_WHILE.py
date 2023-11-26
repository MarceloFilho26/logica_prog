num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

y = 1
while num2 == 0:
    print("Não aceitamos números iguais a zero!")
    num2 = float(input("Digite novamente o segundo número: "))
    y += 1
    if y >= 5:
        print("Programa encerrado!")
        break
else:
    divisao = num1 / num2
    print(divisao)
