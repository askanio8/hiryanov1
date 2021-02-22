class Person:
    some = 3  # Глобальная переменная для всех обьектов

    def __init__(self, name, age):
        self.__name = name  # Инкапсуляция свойства
        self.__age = age

    @property
    def age(self):
        return self.__age  # Геттер

    @age.setter
    def age(self, age):
        self.__age = age  # Сеттер определяется после геттера

    def __del__(self):
        print("deleted")

    def info(self):
        print(self.__name)


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)  # Вызов конструктора базового класса, если базовай класс один


a = Person("dsg", 4)
