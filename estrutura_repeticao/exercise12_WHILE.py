students = int(input("Enter the amount of students: "))
y = 1
soma = 0
while y <= students:
    num = float(input("Enter a note: "))
    soma += num
    y += 1
media = soma / students
print(f"Your average is {media}")


