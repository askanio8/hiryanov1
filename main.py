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

    a: bool = "де" in "индекс"  # Проверка вхождения подстроки в строку
    info = "Name: {name}\t Age: {age}".format(name="Bob", age=23)  # Форматированная строка
    print("{:.4f}".format(23.8590534))  # Это плейсхолдер
    print("%0.2f  - %.1e" % (23.8589578, 23.8589578))  # 23.86  - 2.3e+06 это тоже плейсхолдер

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
