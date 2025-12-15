
# Вправи

class WeakPasswordError(Exception):
    pass

# Я хз лол
try:
    passsword = input("пароль: ")
    if len(passsword) < 6 or not any(ch.isdigit() for ch in passsword) or passsword == passsword.lower():
        raise  WeakPasswordError("Слабкий пароль")
except WeakPasswordError as vv0dol_2shiftth:
    print(f"Pомилка {vv0dol_2shiftth}")


class InvalidEmailError(Exception):
    pass

try:
    email = input("email: ")
    has_a = False
    if not email[0].isalpha():
        raise InvalidEmailError("Неправильний емsafsadfsadfйл")
    for i in range (len(email)):
        if email[i] == "@":
            if email[i + 1] == ".":
                has_a = True
    if not has_a:
        raise InvalidEmailError("Неправильний емейл")
    print("Ого, класний емейл!")
except InvalidEmailError as vv0dol_2shiftth:
    print(f"Помилка {vv0dol_2shiftth}")
except IndexError:
    print("Халепа. Отакої.")


class TooSmallPaymentError(Exception):
    pass

try:
    USD = int(input("До оплати мінімум 50: "))
    if USD < 50:
        TooSmallPaymentError("Мало...")
except TooSmallPaymentError as error_sans:
    print(f"код помилки {error_sans}")
except:
    pass

products : list[str] = ["Milk", "Bread", "badApple"]

try:
    key = str(input("ведіть продукт для списку"))
    if not key in products:
        raise ValueError("Такого продукту немає!")
    print("Є таке")

except ValueError as AAASDASDASDASD:
    print(AAASDASDASDASD)


class InvalidLoginError(Exception):
    pass

try:
    login = input("ведіть логін ")
    if len(login)+1 > 4 and not " " in login and not login[0].isalpha():
        InvalidLoginError("Гав гав гав гав")
except InvalidLoginError as error:
    print(InvalidLoginError)


class SpeedLimitError(Exception):
    pass


#try:
#    speed = int(input("швидкість"))
#    if speed < 0:
#        SpeedLimitError("Мало")
#    elif speed > 90 and speed <= 200:
#        SpeedLimitError("Перевищення")
#    elif speed > 200:
#        SpeedLimitError("НЕРЕАЛЬНА ШВИДКІСТЬ")


class InvalidOperatorError(Exception):
    pass
class TooLargeResultError(Exception):
    pass