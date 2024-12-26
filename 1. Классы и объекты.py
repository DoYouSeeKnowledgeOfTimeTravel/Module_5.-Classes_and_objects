class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


sanya = Human('Саня', 'Кравченко', 43)
kolya = Human('Коля', 'Шальной', 84)
print(sanya.name, sanya.surname, sanya.age)
print(kolya.name, kolya.surname, kolya.age)