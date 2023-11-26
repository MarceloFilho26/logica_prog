diaAtual = int(input("Informe o dia atual:  "))
diaNasc = int(input("Que dia você nasceu? "))
mesAtual = int(input("Informe o mês atual: "))
mesNasc = int(input("Em que mês você nasceu? "))
idade = int(input("Informe a sua idade: "))

diaTotal = diaAtual - diaNasc
mesTotal = mesAtual - mesNasc
totalDias = (idade * 365) + (mesTotal * 30) + diaTotal

print(f"A quantidade de dias é {totalDias}")