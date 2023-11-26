nota1 = 0
nota2 = 0
resp = "S"

print("Não aceitamos notas menor que 0 ou maior que 10!")
while resp == "S":
    nota1 = float(input("Digite sua primeira nota: "))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("Primeira nota inválida. Digite novamente: "))

    nota2 = float(input("Digite sua segunda nota: "))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("Segunda nota inválida. Digite novamente: "))

    media = (nota1 + nota2) / 2
    print(f"Sua média foi {media}")
    resp = input("Deseja fazer um novo cálculo? [S/N]: ")
else:
    print("Programa encerrado!")
