class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set(self):
        print(self.name.title() + '请坐')


class car():
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def read_name(self):
        print(self.name.title())


class Electr_car():
    def __init__(self, name, model, year):
        super().__init__(name, model, year)
