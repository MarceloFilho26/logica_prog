escolha = 0
escolha1 = 0
num = int(input("Informe um número: "))
while escolha != "1" and escolha != "2" and escolha != "3":
    escolha = input("Digite 1 para mostrar o antecessor ou 2 para o sucessor ou 3 para encerrar: ")
    if escolha == "1":
        print(f"O número antecessor ao informado é {num - 1}.")
        escolha1 = (input("Digite 3 para encerrar: "))
    elif escolha == "2":
        print(f"O número sucessor ao informado é {num + 1}.")
        escolha1 = (input("Digite 3 para encerrar: "))
    elif escolha == "3":
        print("Programa encerrado.")
while escolha1 == "3":
    print("Programa encerrado.")
    break