#Варіант 7.2


import random

M = int(input("Введіть кількість рядків (M): "))
N = int(input("Введіть кількість стовпців (N): "))

array = [[random.randint(1, 20) for _ in range(N)] for _ in range(M)]

max_row = max(array, key=sum)

print("Масив: ")
for row in array:
    print(row)

print("Рядок з найбільшою сумою елементів:", max_row)
print("Сума:", sum(max_row))