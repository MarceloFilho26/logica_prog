n = int(input("Digite um número: "))
for x in range(n + 1):
    for y in range(1, x + 1):
        print(y, end=" ")
    print()
