import threading
from queue import Queue  # Это очередь для событий? потоков
import time


# ЕСЛИ ЗАДАЧИ В ПОТОКАХ ВЫЧИСЛИТЕЛЬНЫЕ, БЕЗ ОБРАЩЕНИЙ В БД, ФАЙЛЫ ИЛИ СЕТЬ, ТО ИСПОЛЬЗУЕТСЯ МУЛЬТИПРОЦЕССИНГ
# ЕСЛИ ЕСТЬ ОБРАЩЕНИЯ, НО ПОТОКОВ НЕ МНОГО, ОТВЕТЫ БЫСТРЫЕ ТО МОЖНО ИСПОЛЬЗОВАТЬ THREAD(МНОГОПОТОЧНОСТЬ) ИЛИ АСИНХРОНН
# ЕСЛИ БОЛЬШОЕ ВРЕМЯ ОЖИДАНИЯ ОТВЕТА ИЗВНЕ ИЛИ МНОГО ПОТОКОВ(НАПРИМЕР СЕТЬ) ТО АСИНХРОННОСТЬ
##############################################
class MyThread(threading.Thread):
    def run(self):  # Только run и __init__ можно переопределить в производном классе
        for _ in range(10):
            print(threading.current_thread().getName())



x = MyThread(name="firstThread")
y = MyThread(name="secondThread")
x.start()
y.start()  # Если запустить в режиме дебаг, то вывод немного перемешивается, а если run то не успевает


##############################################
def func(n):
    time.sleep(n)


t1 = threading.Thread(target=func, args=(1,))  # Нужна запятая после первого аргумента
# Потоки с флагом daemon=True завершаются, если не осталось потоков daemon False(например после завершении основного)
# Если потоки используют ресурсы, лучше не делать их демонами, а завершать событием Event
t2 = threading.Thread(target=func, args=(1,), daemon=True)

x1 = time.time()

t1.start()
t2.start()
t1.join()  # Тут главный поток ждет окончания потока t1, без join главный поток продолжит выполняться дальше
t2.join(timeout=2)  # timeout - предельное время ожидания
x2 = time.time()

print(x1 - x2)  # Время выполнения 1 секунда, как и ожидалось

# Количество потоков,значение учитывает внутренние потоки модулей, потоки дебаг, непредсказуемо
print(threading.active_count())
print(threading.current_thread())  # Текущий поток
print(threading.get_native_id())  # Идентификатор потока в ОС
print(list(threading.enumerate()))  # Список выполняющихся потоков
print(threading.main_thread())
mydata = threading.local()  # Переменные класса local являются локальными для текущего потока
mydata.x = 1
