hora1 = int(input("Digite a hora da primeira entrada: "))
minuto1 = int(input("Digite os minutos da primeira entrada: "))
hora2 = int(input("Digite a hora da segunda entrada: "))
minuto2 = int(input("Digite os minutos da segunda entrada: "))
horam = 0

if hora1 >= 12:
    hora1 = hora1 - 12
if hora2 >= 12:
    hora2 = hora2 - 12

minutot = minuto1 + minuto2
if minutot >= 60:
    minutot = minutot - 60
    horam = 1
horat = hora1 + hora2 + horam

if horat >= 12:
    horat = horat - 12

print(f"{horat}:0{minutot}")
