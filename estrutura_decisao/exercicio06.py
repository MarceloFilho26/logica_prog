nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

if nota1 < 0 or nota2 < 0 or nota3 < 0 or nota1 > 10 or nota2 > 10 or nota3 > 10:
    print("Alguma nota foi digitada de forma inválida, digite tudo novamente!")

else:
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        print("Aprovado!")
    else:
        if media >= 4:
            print("Recuperação!")
        else:
            print("Reprovado!")
