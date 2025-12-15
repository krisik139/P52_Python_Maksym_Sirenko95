from enum import StrEnum
from mimetypes import inited


def krasota():
    a = ""
    for j in range(30):
        a += "-"
    for i in range(3):
        print(a)

class MGE:

    def __init__(self,name : str,my_class : str):
        self.name : str = name
        self.my_class : str = my_class
        self.power : int = 100
        self.in_gym : bool = False

    def print_status(self):
        print(f"Ім'я: {self.name}\n"
              f"Клас: {self.my_class}\n"
              f"Сила: {self.power}")

    def gym(self,go_in : bool):
        phrases = {True:"Мге брат йде в залу",
                   False:"Мге брат пішов із залу"}
        print(phrases[go_in])
        self.in_gym = go_in

    def traning(self, how_many : int):
        if self.in_gym:
            self.power += 10*how_many
            print(f"Мге брат зробив {how_many} підходів вправи!")
        else:
            print(f"Мге брат має бути в залі.")


mge_brother : MGE = MGE("Sniper", "sniper")
mge_brother.print_status()
mge_brother.gym(True)
mge_brother.traning(10)
mge_brother.gym(False)


krasota()


class Product:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    def info(self):
        print(f"Назва товару: {self.title}, {self.price}грн, {self.quantity} шт.")

    def total_price(self):
        return int(self.price * self.quantity)

laptop = Product("ASUS gemini edition", 14000, 10)
laptop.info()
print(laptop.total_price())


krasota()


class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def info(self):
        print(f"Це {self.color} {self.model}\n{self.year} року")

drandulet = Car("Драндулет", 1998, "коричневий")
drandulet.info()


krasota()


class Student:
    def __init__(self, name, group, mark):
        self.name = name
        self.group = group
        self.mark = mark

    def marks_info(self):
        print(f"ФІ: {self.name}, Група: {self.group}, Сер. бал: {self.mark}")
        if self.mark > 90:
            print("В ідмінник")
        else:
            print("Пазоріще.")

maksym = Student("Максим Сіренко", 52, 89)
maksym.marks_info()


krasota()


class BankAccount:
    def __init__(self, власник, баланс):
        self.boss = власник
        self.value = баланс

    def withdraw(self, amount):
        if amount <= self.value:
            self.value -= amount
        else:
            print("ти чота попутал")
            return
        print(f"Баланс: {self.value}")

    def deposit(self, amount):
        self.value += amount
        print(f"Баланс: {self.value}")

    def info(self):
        print(self.value)

Maksym_Sirenko = BankAccount("Максим Сіренко", 12034)