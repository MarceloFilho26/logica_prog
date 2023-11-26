HoraInicio = int(input("Informe a hora inicial: "))
HoraFim = int(input("Informe a hora do fim: "))

if HoraInicio >= HoraFim:
    duracao = (24 - HoraInicio) + HoraFim
else:
    duracao = HoraFim - HoraInicio
print(f"A duração do jogo de xadrez é de {duracao} horas.")