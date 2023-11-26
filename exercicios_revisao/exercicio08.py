n = 0
soma = 0
num = int(input("Informe a quantidade: "))
for x in range(num):
    n = float(input("Informe um número: "))
    soma = soma + n
media = soma / num

print(f"A soma entre os número equivale a {soma}.")
print(f"A media entre os número equivale a {media}.")
