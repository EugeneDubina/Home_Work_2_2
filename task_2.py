a = int(input("Введите положительное число из 2 или более цифр: "))
max1 = a % 10
while a >= 1:
    a = a // 10
    if a % 10 > max1:
        max1 = a % 10
    elif a > 9:
        pass
print("Самая большая цифра в числе: ",max1)