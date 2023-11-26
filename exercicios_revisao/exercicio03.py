ano_atual = int(input("Digite o ano atual: "))
idade = int(input("Digite sua idade: "))
mes_nasc = int(input("Digite o mes em que nasceu: "))
mes_atual = int(input("Digite o mes atual: "))

if mes_nasc >= mes_atual:
    nascimento = ano_atual - idade - 1
else:
    nascimento = ano_atual - idade

print(f"Seu ano de nascimento é {nascimento}.")