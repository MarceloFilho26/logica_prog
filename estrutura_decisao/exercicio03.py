aluno = input("Digite seu nome: ")
nota1 = float(input("Dgite a primeira nota: "))
nota2 = float(input("Dgite a segunda nota: "))
media = (nota1 + nota2) / 2
print(aluno, "sua média foi", media)

if media >= 7:
    print("O", aluno, "está aprovado por média.")
elif media >= 4:
    print("O", aluno, "está em recuperação.")
else:
    print("O", aluno, "está reprovado por média.")
