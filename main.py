import turtle
import time
from contracts import contract


@contract(some_name='int,>10')  # Это контракт, условие должно выполняться, иначе exception
def func(some_name: int) -> None:  # Указание типа не влияет на результат выполнения
    """
    Это документ строка функции
    :param some_name: руеквроавпяр
    :return: пкврпсмрвярв
    """
    a: float = "Здесь везде аннотации"  # Аннотации не влияют на результат выполнения
    print(some_name)


if __name__ == '__main__':

    print("индекс ", ord("А"))  # Номер символа в unicode
    a: bool = "де" in "индекс"  # Проверка вхождения подстроки в строку
    info = "Name: {name}\t Age: {age}".format(name="Bob", age=23)  # Форматированная строка
    print("{:.4f}".format(23.8590534))  # Это плейсхолдер
    print("%0.2f  - %.1e" % (23.8589578, 23.8589578))  # 23.86  - 2.3e+06 это тоже плейсхолдер

    import random

    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(numbers)  # Перемешивание списка
    random_number = random.choice(numbers)  # Извлечение случайного элемена

    import math

    math.log(8, 2)  # Логарифм 8 по основанию 2

    for x in 3, 4, 6, 7:
        print(x ** 2)
    for x in range(100, 10, -10):
        print(x ** 2)

    t1 = time.time()
    print(2 ** 1111135)
    t2 = time.time()  # Время исполнения

    print(t2 - t1)

    a, b = 44, 52

    a, b = b, a  # Жонглирование при присваивании

    tup = 1, 2, "привет", 4, 5, 6, 7  # Кортеж tuple неизменяемый

    a, *b, rest = tup  # Распаковка кортежа, *b становится типом list

    print(a, b)
    print(type(b))
    print(*b, sep=":", end="!\n")  # Печать кортежа с разделителем
    func("3fs")

    for i, angle in enumerate(tup):  # Так счетчик добавляется сам второй переменной
        print(i, ":", angle)

    mn = {"donetsk", "minsk", "berlin"}  # Неупоорядоченное изменяемое(хотя есть и frozen set) множество set
    if "minsk" in mn:  # Проверка вхождения элемента здесь выполняется быстрее, элементы уникальны
        mn.add(22)
    mn - mn  # Разность множеств
    mn & mn  # Пересечение и тд
    mn.issubset(mn)  # Проверка является ли одно множество подмножеством другого
    mn.issuperset(mn)  # Надмножеством
    mn.union(mn)

    md = {"donetsk": 33, "minsk": 22, "berlin": 11}  # А это словарь dict, только ключ уникален
    md["rostov"] = 55  # Добавление в словарь
    print(md)

    '''rahgsjfyskjgdhnaer ths frhfd sh srthfg
    h sftdhf gxhj fgh ftgh ert
    dtrh cfgh xfg h
    dtfhf xhj xyfjyftxjn'''  # Это просто многострочная строка

    try:
        param = int(input())
    except Exception as e:
        print("err:", e)
        raise Exception("myExeption")  # Свое исключение                    !!!! ДАЛЬШЕ КОД НЕ СРАБАТЫВАЕТ
    finally:
        print("fin")

    numbers = [7] * 5  # Инициализация списка
    numbers1 = list(range(10, 2, -2))  # В numpy есть еще arange это про диапазон

    companies = ["Microsoft", "Google", "Oracle", "Apple"]
    item = "Oracle"  # Элемент для удаления
    if item in companies:  # Если применить remove без проверки наличия элемента может выбросить exeption
        companies.remove(item)

    users = ["Tom", "bob", "alice", "Sam", "Bill"]
    users.sort(key=str.lower)  # Сортируест список с учетом регистра с ключом lower
    sorted_users = sorted(users, key=str.lower)  # Sorted в отличии от sort не изменяет  исходный список
    # users2 = copy.deepcopy(users1) # Глубокое копирование списка(если список вложенный), если нет, то просто copy
    users.pop(-1)  # Синтаксис удаления элеента списка

    user = ("Tom",)  # Инициализация кортежа
    users_tuple = tuple(users)  # Конвертация списка в кортеж

    users = {
        "+11111111": "Tom",
        "+33333333": "Bob",
        "+55555555": "Alice"
    }

    del users["+55555555"]  # Удаление элемента из словаря по ключу, нужна проверка if x in X

    for key in users:  # Варианты перебора словарей
        print(key, " - ", users[key])

    for key, value in users.items():
        print(key, " - ", value)

    for value in users.values():
        print(value)

    for value in users.values():
        print(value)

    with open("hello.txt",
              "r", encoding="utf8") as somefile:  # Такая конструкция не генерирует исключение и закрывает файл в конце
        somefile.read()

    with open("C:\\Users\\Admin\\Desktop\\fgsd", "w+") as f:
        f.write("gdx")

    import csv

    columns = ["name", "age"]
    writer = csv.DictWriter(open("gfd", "w", newline=""), fieldnames=columns)  # Запись в csv словаря dict
    writer.writeheader()
    users = [
        {"name": "Tom", "age": 28},
        {"name": "Alice", "age": 23},
        {"name": "Bob", "age": 34}
    ]
    writer.writerows(users)  # Запись нескольких строк
    # writer.writerow(user)  # Запись одной строки

    import pickle  # Чтение и запись бинарных обьектов в файлы
    import shelve  # Чтение и запись бинарных обьектов в файлы c этой библиотекой лучше

    FILENAME = "user.dat"
    name = "Tom"
    age = 19
    with open(FILENAME, "wb") as file:
        pickle.dump(name, file)
        pickle.dump(age, file)
    with open(FILENAME, "rb") as file:
        name = pickle.load(file)
        age = pickle.load(file)
        print("Имя:", name, "\tВозраст:", age)

    eval("2 + 3*len('hello')") # Выполняет строку как код, осторожно!

    input()
