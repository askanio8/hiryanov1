import turtle
import time


def func(some_name: int) -> None:  # указание типа не влияет на результат выполнения
    """
    это документ строка функции
    :param some_name: руеквроавпяр
    :return: пкврпсмрвярв
    """
    a: float = "Здесь везде аннотации"  # аннотации не влияют на результат выполнения
    print(some_name)


if __name__ == '__main__':

    print("индекс ", ord("А"))  # номер символа в unicode
    a: bool = "де" in "индекс"  # проверка вхождения подстроки в строку
    info = "Name: {name}\t Age: {age}".format(name="Bob", age=23)  # форматированная строка
    print("{:.4f}".format(23.8590534))  # это плейсхолдер
    print("%0.2f  - %.1e" % (23.8589578, 23.8589578))  # 23.86  - 2.3e+06 это тоже плейсхолдер

    import random
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(numbers)  # перемешивание списка
    random_number = random.choice(numbers)  # извлечение случайного элемена

    import math
    math.log(8, 2)  # логарифм 8 по основанию 2


    for x in 3, 4, 6, 7:
        print(x ** 2)
    for x in range(100, 10, -10):
        print(x ** 2)

    t1 = time.time()
    print(2 ** 1111135)
    t2 = time.time()  # время исполнения

    print(t2 - t1)

    a, b = 44, 52

    a, b = b, a  # жонглирование при присваивании

    tup = 1, 2, "привет", 4, 5, 6, 7  # кортеж tuple неизменяемый

    a, *b, rest = tup  # распаковка кортежа, *b становится типом list

    print(a, b)
    print(type(b))
    print(*b, sep=":", end="!\n")  # печать кортежа с разделителем
    func("3fs")

    for i, angle in enumerate(tup):  # так счетчик добавляется сам второй переменной
        print(i, ":", angle)

    mn = {"donetsk", "minsk", "berlin"}  # неупоорядоченное изменяемое(хотя есть и frozen set) множество set
    if "minsk" in mn:  # проверка вхождения элемента здесь выполняется быстрее, элементы уникальны
        mn.add(22)
    mn - mn  # разность множеств
    mn & mn  # пересечение и тд
    mn.issubset(mn)  # проверка является ли одно множество подмножеством другого
    mn.issuperset(mn)  # надмножеством
    mn.union(mn)

    md = {"donetsk": 33, "minsk": 22, "berlin": 11}  # а это словарь dict, только ключ уникален
    md["rostov"] = 55  # добавление в словарь
    print(md)

    '''rahgsjfyskjgdhnaer ths frhfd sh srthfg
    h sftdhf gxhj fgh ftgh ert
    dtrh cfgh xfg h
    dtfhf xhj xyfjyftxjn'''  # это просто многострочная строка

    try:
        param = int(input())
    except Exception as e:
        print("err:", e)
        raise Exception("myExeption")  # свое исключение                    !!!! ДАЛЬШЕ КОД НЕ СРАБАТЫВАЕТ
    finally:
        print("fin")

    numbers = [7] * 5  # инициализация списка
    numbers1 = list(range(10, 2, -2))  # в numpy есть еще arange это про диапазон

    companies = ["Microsoft", "Google", "Oracle", "Apple"]
    item = "Oracle"  # элемент для удаления
    if item in companies:  # если применить remove без проверки наличия элемента может выбросить exeption
        companies.remove(item)

    users = ["Tom", "bob", "alice", "Sam", "Bill"]
    users.sort(key=str.lower)  # сортируест список с учетом регистра с ключом lower
    sorted_users = sorted(users, key=str.lower)  # sorted в отличии от sort не изменяет  исходный список
    # users2 = copy.deepcopy(users1) # глубокое копирование списка(если список вложенный), если нет, то просто copy
    users.pop(-1)  # синтаксис удаления элеента списка

    user = ("Tom",)  # инициализация кортежа
    users_tuple = tuple(users)  # конвертация списка в кортеж

    users = {
        "+11111111": "Tom",
        "+33333333": "Bob",
        "+55555555": "Alice"
    }

    del users["+55555555"]  # удаление элемента из словаря по ключу, нужна проверка if x in X

    for key in users:  # варианты перебора словарей
        print(key, " - ", users[key])

    for key, value in users.items():
        print(key, " - ", value)

    for value in users.values():
        print(value)

    for value in users.values():
        print(value)

    with open("hello.txt",
              "r", encoding="utf8") as somefile:  # такая конструкция не генерирует исключение и закрывает файл в конце
        somefile.read()

    with open("C:\\Users\\Admin\\Desktop\\fgsd", "w+") as f:
        f.write("gdx")

    import csv

    columns = ["name", "age"]
    writer = csv.DictWriter(open("gfd", "w", newline=""), fieldnames=columns)  # запись в csv словаря dict
    writer.writeheader()
    users = [
        {"name": "Tom", "age": 28},
        {"name": "Alice", "age": 23},
        {"name": "Bob", "age": 34}
    ]
    writer.writerows(users)  # запись нескольких строк
    # writer.writerow(user)  # запись одной строки

    import pickle  # чтение и запись бинарных обьектов в файлы
    import shelve  # чтение и запись бинарных обьектов в файлы c этой библиотекой лучше

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

    input()
