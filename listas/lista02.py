alunos = []
n = int(input("Informe a quantidade de alunos: "))
for x in range(n):
    alunos.append(input("Informe o nome do aluno: "))
for i in range(n):
    print(alunos[i], f"está na posição aluno[{i}] do array e seu rank é {i + 1}.")