n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

if n1 > n2:
    if n2 > n3:
        print("N1 é o maior!")
    else:
        print("N2 é o maior!")
else:
    if n2 > n3:
        print("N2 é o maior!")
    else:
        print("N3 é o maior!")
