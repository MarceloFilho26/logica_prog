nome = input("Digite seu nome: ")
while len(nome) <= 3:
    nome = input("Seu nome deve conter mais que três caracteres: ")
idade = int(input("Digite sua idade: "))
while (idade < 0) or (idade > 150):
    idade = int(input("Sua idade deve conter de 0 a 150: "))
salario = float(input("Digite seu salário: "))
while salario < 0:
    salario = float(input("Digite seu salário novamente: "))
sexo = input("Digite seu sexo utilizando 'f' papra feminino e 'm' para masculino: ")
while (sexo != 'f') and (sexo != 'm'):
    sexo = input("Digite novamente, sendo 'f' para femenino e 'm' para masculino: ")
estado_civil = input("Digite seu estado civil, utilize 's', 'c', 'v' ou 'd': ")
while (estado_civil != 's') and (estado_civil != 'c') and (estado_civil != 'v') and (estado_civil != 'd'):
    estado_civil = input("Digite novamente: ")

print("Cadastro realizado com sucesso!")
