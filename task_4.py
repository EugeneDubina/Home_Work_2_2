n = int(input("Введите количество элементов в списке: "))
list_1 = input("Введите элементы через пробел: ").split()
i = 0

for i in range(0, len(list_1)-1, 2):
    list_1[i], list_1[i+1] = list_1[i+1], list_1[i]

print(list_1)