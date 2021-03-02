from multiprocessing import Process, Queue
import os
import time

workers_number = 4
FIB = 40


def worker(tasks: Queue, answers: Queue, process_index: int):  # Queue - FIFO !!!
    def fib(n: int) -> int:
        return fib(n - 1) + fib(n - 2) if n > 2 else 1

    while not tasks.empty():  # Все 4 процесса будут в цикле пока не достанут все из tasks
        number = tasks.get()  # Забираем из очереди набор аргументов и распаковываем
        answer = fib(number)
        answers.put((process_index, os.getpid(), number, answer,))  # Обратная очередь в главный поток
        #print(f"worker {precess_index}, PID={os.getpid()}: fib({number}) = {answer}")


def main():
    tasks = Queue()  # Очередь - это просто список наборов аргументов или классов для потока
    answers = Queue()
    for n in range(0, FIB + 1):
        tasks.put(n)  # Добавляем аргумент в список

    workers = []  #
    for process_index in range(workers_number):
        worker_process = Process(target=worker, args=(tasks, answers, process_index,))  # Кол-во роцессов = кол-ву потоков ядер
        workers.append(worker_process)  # target - ф-я для параллельного выполнения, tasks - кол-во задач для неё
    print("процессы готовы")
    start_time = time.perf_counter()
    for worker_process in workers:
        worker_process.start()  # Стартуем 4 процесса
    print("процессы запущены")
    for worker_process in workers:
        worker_process.join()  # Ждем все 4 процесса тут
    print(time.perf_counter() - start_time)

    while not answers.empty():  # Достаём ответы
        process_index, getpid, number, answer = answers.get()
        print(f"worker {process_index}, PID={getpid}: fib({number}) = {answer}")

if __name__ == '__main__':
    main()

# parent_conn, child_conn = Pipe() Двунаправленная труба, имеющая методы send, recv

# lock = Lock() метод синхронизации доступа, как в threading. те же методы acquire и release
# multiprocessing.Event
# multiprocessing.Condition
# multiprocessing.BoundedSemaphore
# multiprocessing.Barrier
# multiprocessing.RLock

# num = Value('d', 0.0)  # Классы для взаимодействия процессов, создают общие объекты
# arr = Array('i', range(10))
# with Manager() as manager

# multiprocessing.active_children()
# multiprocessing.cpu_count()
# multiprocessing.get_all_start_methods() Для того чтобы найти подходящий метод запуска в зависимости от ОС
