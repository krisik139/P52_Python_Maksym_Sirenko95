from platform import libc_ver
from random import *


class Student:

    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.is_alive = True

    def to_study(self):
        print("Ми вчимося")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("и спеимо")
        self.gladness += 1

    def to_chill(self):
        print("Ми відпочиваємо")
        self.gladness += 2
        self.progress -= 0.1

    def is_alive_func(self):
        if self.progress < -0.5:
            print("Вилючено")
            self.is_alive = False

        elif self.gladness <= 0:
            print("ZXC дота, пофіг на навчання")
            self.is_alive = False

        elif self.progress > 5:
            print("Пройшли...")
            self.is_alive = False

    def end_of_day(self):
        print(f"Щасться = {self.gladness}\n"
              f"Прогресія = {self.progress}")

    def live(self, day):
        print(f"День {day}")
        live_cube = randint(1,3)

        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()

        self.end_of_day()
        self.is_alive_func()



student1 = Student("Maksym Sirenko")

for day in range(365):
    if student1.is_alive == False:
        break

    student1.live(day)