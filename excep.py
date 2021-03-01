import traceback
from threading import Lock


try:
    raise Exception('fsdg', 'gfsdhgs')
except Exception as e:
    print(e.args)
    traceback.print_tb(e.__traceback__)  # Покажет стек вызовов и аргументы exception


my_lock = Lock()
try:  # Все равно что обернуть это в my_lock.acquire() my_lock.release()
    with my_lock, open("filename", 'r') as f:  # Так не возникают блокировки при исключении
        "somelist".append(f.read())
except:
    print('Encountered an exception...')