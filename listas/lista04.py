numbers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
infousu = int(input("Informe um número: "))
M = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10):
    M[i] = numbers[i] * infousu

print(numbers)
print(f"x {infousu}")
print(M)