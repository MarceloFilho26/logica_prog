tipo_combustivel = input("Digite G para gasolina e E para Etanol: ")
litros_abastecido = float(input("Digite o valor de litros abastecido: "))

if tipo_combustivel == 'G' or tipo_combustivel == 'g':
    print("Você selecionou a Gasolina.")
    valor_pagar = litros_abastecido * 5.80
    print("O valor a ser pago será de: ", valor_pagar)

elif tipo_combustivel == 'E' or tipo_combustivel == 'e':
    print("Você selecionou o Etanol.")
    valor_pagar = litros_abastecido * 4.90
    print("O valor a ser pago será de: ", valor_pagar)
else:
    print("Você selecionou o tipo de combustível incorretamente, por favor tente novamente.")
