# А ви знали що try це спробувати
try:
    #небезпечний код
    #age = int(input("Введи свій вік: "))
    int("a")

except ValueError:
    #безпечний код
    print("typoi...")



try:
    # небезпечний код
    int("Введи свій вік: ")

except Exception as error:
    # безпечний код
    print("Мені навіть умови не потрібно щоб засрати тебе")
    print(f"Enjoy the fireworks - {error}")



try:
    # небезпечний код
    age = int(input("Введи свій вік: "))
    age/0

except (ValueError, ZeroDivisionError):
    # безпечний код
    print("Мені навіть 3 умов не потрібно щоб засрати тебе")
    print(f"Don't enjoy the fireworks")



try:
    a = int(input("ніж далі в ліс, тим elif elif"))

except (ZeroDivisionError):
    print("ага! Спіймав за сракатан")

else:
    print("Чо ряльна?")

finally:
    print("Давайте к ой блин закончим")