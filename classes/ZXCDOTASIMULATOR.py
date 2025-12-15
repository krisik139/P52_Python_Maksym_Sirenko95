from random import *

class Ingir:
    def __init__(self, knowledge):
        self.knowledge = knowledge
        self.stress = 10
        self.rocket_progress = 0
        self.alive = True

    def design_rocket(self):
        print("Роблю ракету")
        self.rocket_progress += randint(1,3)
        self.stress += 2

    def study_space(self):
        print("Вивчаю космос")
        self.knowledge += randint(2,3)
        self.stress += 3

    def team_meeting(self):
        print("Розмовляю з командою")
        self.rocket_progress += randint(2,3)
        self.stress -= 1

    def rest(self):
        print("Відпочиваю")
        self.stress -= randint(3,5)

    def work(self):
        to_do = randint(0, 3)
        match to_do:
            case 0:
                self.design_rocket()
            case 1:
                self.study_space()
            case 2:
                self.team_meeting()
            case 3:
                self.rest()

    def live_day(self, day, actuality):

        if self.knowledge < actuality:
            self.alive = False
            print("Знання тепер не актуальні")
            return

        elif self.stress > 50:
            self.alive = False
            print("Забагато стресу")
            return

        elif self.rocket_progress > 100:
            self.alive = False
            print("Ракета запущена!")
            return

        self.work()
        print(f"День {day}")
        print(f"Знання: {self.knowledge}\n"
              f"Стресс: {self.stress}\n"
              f"Прогрессс: {self.rocket_progress}")

maksym = Ingir(10)

day = 0
actuality = 0
while True:
    maksym.live_day(day, actuality)
    actuality += randint(0,1)
    day += 1
    if maksym.alive == False:
        break