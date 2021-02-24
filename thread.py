import threading
from queue import Queue  # Это очередь для событий? потоков
import time


class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
