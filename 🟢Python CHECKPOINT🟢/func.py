def is_even(n):
    return n % 2 == 0

def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total

nums = [23,32,35,2342,32,32]
print(f"Cума: {sum_list(nums)}")


class Student:
    def __init__(self):
        self.name = "Maksym"
        self.grades = []

    def add_grade(self, g):
        self.grades.append(g)

    def avarge(self):
        if not self.grades:
            return sum(self.grades)/len(self.grades)

    def info(self):
        print(self.name,"Сер біл",self.avarge())