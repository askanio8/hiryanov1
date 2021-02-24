s = []
print(s[-1:])  # Если список пустой, то исключения не будет, такой срез вернет пустой список

a = (1, 'gfd', 3.54)  # Это кортеж, скобки не обязательны

с, *b, rest = a  # Распаковка кортежа, *b становится типом list

print(с, b)
print(type(b))
print(*b, sep=":", end="!\n")  # Печать кортежа с разделителем

tup = 1, 1.2, 'fgds'

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

users = ["Tom", "bob", "alice", "Sam", "Bill"]
users.sort(key=str.lower)  # Сортируест список с учетом регистра с ключом lower
sorted_users = sorted(users, key=str.lower)  # Sorted в отличии от sort не изменяет  исходный список
# users2 = copy.deepcopy(users1) # Глубокое копирование списка(если список вложенный), если нет, то просто copy
users.pop(-1)  # Синтаксис удаления элеента списка

numbers = [7] * 5  # Инициализация списка
numbers1 = list(range(10, 2, -2))  # В numpy есть еще arange это про диапазон

companies = ["Microsoft", "Google", "Oracle", "Apple"]
item = "Oracle"  # Элемент для удаления
if item in companies:  # Если применить remove без проверки наличия элемента может выбросить exeption
    companies.remove(item)

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


import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)  # Перемешивание списка
random_number = random.choice(numbers)  # Извлечение случайного элемена
