qtd = 0
soma = 0
for x in range(10):
    num = int(input("Digite os valores: "))
    if num < 0:
        qtd += 1
        print(f"O {num} é negativo.")
        soma += num
p = 10 - qtd

print(f"A quantidade de números negativos é {qtd} e positivos {p}.")
print(f"A somatória dos números equivale a {soma}")
