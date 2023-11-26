while True:
    login = input("Login: ")
    senha = input("Senha: ")

    if login == senha:
        print("A senha não pode ser igual ao login, tente novamente!")
    else:
        print("Cadastro aprovado!")
    break
