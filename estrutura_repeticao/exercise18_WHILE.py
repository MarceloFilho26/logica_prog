n = int(input("Digite um número: "))

x = 0
while x < n + 1:
    x += 1
    y = 1
    while y < x:
        print(y, end=" ")
        y += 1
    print()