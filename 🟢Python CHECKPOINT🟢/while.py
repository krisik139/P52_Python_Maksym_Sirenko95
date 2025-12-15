# ЗАДАЧА 1

import math

n_numbers : int = int(input("Кількість чисел"))
array : list = []


for i in range(n_numbers):
    number : int = int(input("Число"))
    array.append(number)

result = sum(array) / len(array)
print(f"Середнє {result}")


# ЗАДАЧА 2


values : list = input("Введіть список чисел через пробіл").split(" ")

print(f"Мінімально: {min(values)} Максимально: {max(values)}")


# ЗАДАЧА 3


new_list : list = input("Введіть список чисел через пробіл").split(" ")
newest_list = []

for i in range(len(new_list)):
    if new_list[i] % 2 == 0:
        newest_list.append(new_list[i])

print(f"список з парними: {newest_list}")


# ЗАДАЧА 4


array = []
while True:

    line : str = input("Введіть речення(для кінця введіть stop)")
    if line != "stop":
        array.append(line)
    else:
        break

longest = ""
for line in array:
    if len(line) > len(longest):
        longest = line

print(f"Найдовший {longest}, кількість {len(array)+1}")


# ЗАДАЧА 5


string : str = str(input("Введіть рядок"))
aey = ["У","е","і","ї","а","о","є","я","и","ю"]
value : int = 0
for i in range(len(string)):
    if string[i] in aey:
        value += 1
print(f"{value} голосних")


# ЗАДАЧА 6


number = 0

while True:

    match int(input("Виберіть опцію\n1) додати число, 2) показати всі, 3) показати суму. 0 - кінець")):

        case 1:
            number += int(input("Скільки?"))
        case 2:
            print("всі")
        case 3:
            print(number)
        case 0:
            break


# ЗАДАЧА 7


array : list = [2,5,3,6,7,4,10,1]

wrong = 0
last = 0
while True:
    wrong = 0
    last = 0
    for i in range(len(array)):
        if array[i] < last:
            array[i-1] = array[i]
            array[i] = last
            wrong += 1
        last = array[i]
    if wrong == 0:
        break
print(array)