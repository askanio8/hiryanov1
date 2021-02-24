A = range(20)

B = (x ** 2 for x in A if x % 2 == 0)

print(*B)


def f1():
    pass


def f2(a, n):
    return f1  # Функция может возвращать функцию


for i in f1, f2:  # Можно итерироваться по функциям
    f2(f1, 1)  # и передавать функцию как параметр

# Выполняет функцию для каждого элемента и возвращает итератор с результатами
C = map(f2, A)  # Но лучше делать так B = (x**2 for x in A if x % 2 == 0)

print(*(map(lambda x: x ** 2, A)))  # Здесь лямбда функция

D = zip(A, B)  # Возвращает итератор кортежей A[x], B[x]


def arithm_progression(start, stop, step):  # yield x возвращает значение последовательно по запросу
    x = start
    while x < stop:
        yield x
        x += step

E = arithm_progression(1, 10, 1)
for x in E:
    print(x)

F = [a**2 for a in A if a > 2]  # Это генератор, он работет быстрее чем цикл с range
