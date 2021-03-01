from multiprocessing import Pool
import time

workers_number = 4
FIB = 40

# Можно использовать библиотеку C для кратного ускорения
def fib(n: int) -> int:
    return fib(n - 1) + fib(n - 2) if n > 2 else 1


def main():
    tasks = list(range(1, FIB + 1))
    start_time = time.perf_counter()

    with Pool(workers_number) as pool_of_processes:  # В пул передаём количество ядер
        answers = list(pool_of_processes.map(fib, tasks))  # Даём функцию и наборы параметров, получаем ответы

    print(time.perf_counter() - start_time)
    print(*answers)


if __name__ == '__main__':
    main()
