class Person:
    some = 3  # глобальная переменная для всех обьектов

    def __init__(self, name, age):
        self.__name = name  # инкапсуляция свойства
        self.__age = age

    @property
    def age(self):
        return self.__age  # геттер

    @age.setter
    def age(self, age):
        self.__age = age  # сеттер определяется после геттера

    def __del__(self):
        print("deleted")

    def info(self):
        print(self.__name)


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)  # вызов конструктора базового класса, если базовай класс один


a = Person("dsg", 4)
