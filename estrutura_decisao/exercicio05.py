num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 == num2:
    print("Números iguais!")

else:
    if num1 > num2:
        print(num2, num1)
    else:
        print(num1, num2)