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
        raise Exception("myExeption")  # свое исключение
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

    user = ("Tom",) # инициализация кортежа
    users_tuple = tuple(users)  # конвертация списка в кортеж

    users = {
        "+11111111": "Tom",
        "+33333333": "Bob",
        "+55555555": "Alice"
    }

    del users["+55555555"] # удаление элемента из словаря по ключу, нужна проверка if x in X

    for key in users:  # варианты перебора словарей
        print(key, " - ", users[key])

    for key, value in users.items():
        print(key, " - ", value)

    for value in users.values():
        print(value)

    for value in users.values():
        print(value)

 
    input()
