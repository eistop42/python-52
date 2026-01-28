class Programmer:
    def __init__(self, name, grade):
        self.work_time = 0
        self.name = name
        self.grade = grade
        self.all_money = 0
        self.bonus = 0
        self.GRADES_MONEY = {'Junior': 10, 'Middle': 15, 'Senior': 20}

    def work(self, time):
        if self.grade not in self.GRADES_MONEY:
            raise ValueError('Неверный грейд')
        money = time * (self.GRADES_MONEY[self.grade] + self.bonus)
        self.all_money += money

    def rise(self):
        # Повышать с junior > middle, middle > senior
        if self.grade == 'Junior':
            self.grade = 'Middle'
        elif self.grade == 'Middle':
            self.grade = 'Senior'
        elif self.grade == 'Senior':
            self.bonus += 1

    def info(self):
        return f'{self.name} {self.work_time}ч. {self.all_money}тгр.'

programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())