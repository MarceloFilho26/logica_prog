time1 = input("Digite o nome do primeiro time: ")
Gols1 = int(input(f"Digite o número de gols marcados pelo {time1}: "))
time2 = input("Digite o nome do segundo time: ")
Gols2 = int(input(f"Digite o número de gols marcados pelo {time2}: "))

if Gols1 == Gols2:
    print("EMPATE!")
else:
    if Gols1 > Gols2:
        print("O time do", time1, "foi o vencedor!")
    else:
        print("O time do", time2, "foi o vencedor!")
