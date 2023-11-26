key_salva = "C@sa9682"
key = input("Digite sua senha: ")

cont = 1
while key_salva != key:
    key = input(f"Senha incorreta. Restam {3-cont} tentativas. Digite novamente: ")
    cont += 1
    if cont >= 3 and key != key_salva:
        print("Senha bloqueada!")
        break
else:
    print("Login efetuado com sucesso!")
print("Programa finalizado.")
