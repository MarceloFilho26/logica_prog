macas = int(input("Informe a quantidade comprada: "))

if macas < 12:
    total = 1.30 * macas
else:
    total = 1 * macas
print(f"O valor a ser pago é de R${total}.")