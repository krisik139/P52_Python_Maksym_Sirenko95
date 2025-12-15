try:

    number = int(input("ведіть число через пробіл "))

except ValueError:

    print("Помилка, потрібно вводити тільки число")



try:

    number1 = int(input("ведіть число 1 "))
    number2 = int(input("ведіть число 2 "))

    number1/number2

except ValueError:
    print("Введено не те число")

except ZeroDivisionError:
    print("Ділення на нуль не припустиме")



colors = ["red", "green", "blue"]
try:
    index = int(input("ведіть індекс для списку(0-2): "))
    print(colors[index])

except ValueError:
    print("Чота не то число ти вписав")

except IndexError:
    print("Індекс чота за межами")



student = {"name": "Anna", "age": 16}

try:
    key = input("ведіть ключ для словника")
    print(student[key])

except KeyError:
    print("Я не знайшов твій ключ")


_file = None
try:
    file = input("Вкажіть назву файлу")
    _file = open(file, "r")
    print("Так, Є! Закриваю...")
    _file.close()
except:
    print("Ойой! Файла не існує")
    _file.close()



try:
    number = int(input("Чот якесь число введіть "))
    number**2
except ValueError:
    print("Щось не так з крвадратом, може це круг?")



try:
    number1 = int(input("ведіть число 1 "))
    number2 = int(input("ведіть число 2 "))
    number1 * number2

except(TypeError, ValueError):
    print("З тобою щось не так")



try:
    number = int(input("Чот якесь число введіть "))
    if number % 2 == 0:
        print("О да, парне")
except ValueError:
    print("Щось не так з крвадратом, може це круг?")