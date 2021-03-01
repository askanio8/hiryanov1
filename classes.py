from abc import ABC, abstractmethod
import traceback


class Person:
    some = 3  # Глобальная(статическая) переменная для всех обьектов

    def __init__(self, name, age):
        self.__name = name  # Инкапсуляция свойства
        self.__age = age

    @property  # Если нет обработки значения, лучше просто использовать публичное поле, а если понадобится добавить это
    def age(self):
        return self.__age  # Геттер

    @age.setter
    def age(self, age):
        self.__age = age  # Сеттер определяется после геттера

    def __del__(self):  # Кроме del есть методы операций, сравнения, счетчик и тд
        print("deleted")

    def info(self):  # Экземплярный метод
        print(self.__name)
        return 1

    @staticmethod
    def somemetod():  # Статический метод, нельзя переопределить в потомке
        pass

    @classmethod
    def anothermethod(cls, param1, param2):  # Классовый метод, в параметре сам класс, можно переопределить в child
        return cls(param1, param2)  # Может использоваться для "перегрузки" конструктора


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)  # Вызов конструктора базового класса, если базовай класс один
        
    def info(self):
        print(super().info() * 2)  # Переопределение метода при наследовании


class Animals(ABC):

    def draw(self):  # Это обычный метод, его можно переопределить в производном классе
        print("draw animal")

    @abstractmethod
    def move(self):  # Это абстрактный метод, его надо переопределить
        pass


a = Student("dsg", 4)