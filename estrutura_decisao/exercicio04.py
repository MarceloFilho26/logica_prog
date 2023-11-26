nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
filho = int(input("Digite a quantidade de filhos: "))
salario = float(input("Digite o seu salário: "))
porcentagem = float(input("Digite a porcentagem do aumento: "))
salario_porcentagem = salario + (salario * (porcentagem / 100))
ferias = int(salario_porcentagem / 3)
salario_ferias = salario_porcentagem + ferias
imposto_renda = salario_porcentagem * 0.15
desconto_inss = salario_porcentagem * 0.08
abono = salario_porcentagem + (filho * 150)
abono1 = filho * 150
salario_final = (salario_ferias + abono1) - (imposto_renda + desconto_inss)

print("Seu nome: ", nome)
print("Sua idade: ", idade)
print("Seu salário é de R$: ", salario)
print("Seu salário com o aumento é de R$: ", salario_porcentagem)
print("Seu desconto do imposto de renda equivale a R$: ", imposto_renda)
print("Seu desconto de INSS equivale a R$: ", desconto_inss)
print("Seu salário com a adição do abono é de R$: ", abono)
print("Seu 1/3 das férias equivale a R$: ", ferias)
print("Seu salário mais 1/3 das férias equivale a R$: ", salario_ferias)
print("Seu salário final equivale a R$: ", salario_final)
