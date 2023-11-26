num = int(input("Informe um número diferente de zero: "))

if num == 0:
    print("Número inválido!")
else:
    if num < 0:
        print(f"O número {num} é negativo.")
    else:
        print(f"O número {num} é positivo.")