# ЗАДАЧА 1


password : str = input("Введіть пароль.")

if len(password) <= 5:
    print("Не надійний")
elif 5 < len(password) < 10:
    print("Нормальний пароль")
else:
    print("Хороший та надійний пароль")


# ЗАДАЧА 2


km : float = float(input("ведіть скільки кілометрів хочете проїхати."))

price = 60
if km > 2:
    price += (km-2)*15

print(f"До оплати {price}")


# ЗАДАЧА 3


balance : int = int(input("Ваш баланс"))
withdraw : int = int(input("Сума виведення"))

if withdraw > balance:
    print("Недостатньо коштів")
else:
    balance -= withdraw


# ЗАДАЧА 4


step1 : str = input("Камінь-ножиці-папір").lower()
step2 : str = input("Камінь-ножиці-папір").lower()

if step1 == "ножниці" and step2 == "папір":
    print("Гравець 1 перемагає")
elif step2 == "папір" and step1 == "ножниці":
    print("Гравець 2 перемагає")

elif step1 == "камінь" and step2 == "папір":
    print("Гравець 2 перемагає")
elif step2 == "папір" and step1 == "камінь":
    print("Гравець 1 перемагає")

elif step1 == "камінь" and step2 == "ножниці":
    print("Гравець 1 перемагає")
elif step2 == "ножниці" and step1 == "камінь":
    print("Гравець 2 перемагає")


# ЗАДАЧА 5


mark : int = int(input("Введіть ваш бал"))

if mark < 20:
    print("F")
elif 20 <= mark < 40:
    print("D")
elif 40 <= mark < 60:
    print("C")
elif 60 <= mark < 80:
    print("B")
else:
    print("A")
