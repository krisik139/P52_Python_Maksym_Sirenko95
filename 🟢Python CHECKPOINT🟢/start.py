# ЗАДАЧА 1


price : float = float(input("Ведіть ціну товару:"))
value : float = float(input("Введіть оплату"))

left : float = value - price
print(f"Повертаємо вам {round(left,2)} гривень.")


# ЗАДАЧА 2


hours : int = int(input("Ведіть години:"))
minutes : int = int(input("Введіть хвилини"))

from_12 : int = hours*60 + minutes

print(f"Від початку доби прийшло {from_12} хвилин")


# ЗАДАЧА 3


name : str = str(input("Введіть ім'я"))
city : str = str(input("Введіть місто"))

print(f"Привіт, {name} із міста {city}")


# ЗАДАЧА 4


cel : float = float(input("ведіть температуру у цельсіях"))
f : float = cel*1.8+32


print(f"Ваші {cel} цельсія дорівнюють {f} форенгейтам")


# ЗАДАЧА 5


try:

    value_1 : float = float(input("Значення 1"))
    print(f"Перше значення конвертується! {int(value_1)}")
    value_2: float = float(input("Значення 2"))
    print(f"Друге значення конвертується! {int(value_2)}")

except:

    print("Не виходить перевести...")

