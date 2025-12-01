for i in range(1, 11):
    i_2 = i**2
    print(f"квадрат {i} = {i_2}")

for i in range (1,6):
    string = str(i)
    print(string*i)

passwords = ["qwerty", "qwerty123", "maksym1", "mge_brother", "gym_boss", "i_love_dota", "i_gonna_get_a_grip", "snowgrave"]
for i in range(len(passwords)):
    if len(passwords[i]) >= 7:
        print(f"пароль {passwords[i]} є надійним")
    else:
        print(f"пароль {passwords[i]} не є надійним")

likes = [2, 30, 12, 6, 9]
middle = 0

for i in range(len(likes)):
    middle += likes[i]

middle / len(likes)

for i in range(len(likes)):
    if likes[i] > int(middle):
        print(f"Пост {i+1} має більше середнього лайків")
    elif likes[i] == int(middle):
        print(f"Пост {i+1} має середнє значення лайків")
    else:
        print(f"Пост {i+1} має менше значення лайків ніж середнє")

days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Нд"]
plan = ["кардіо", "прес", "біг", "відпочинок", "спина", "ноги", "йога"]

for i in range(len(days)):
    if plan[i][-1] != "а":
        print(f"сьогодні {days[i]}, на сьогодні заплановано {plan[i]}")
    else:
        print(f"сьогодні {days[i]}, на сьогодні запланована {plan[i]}")