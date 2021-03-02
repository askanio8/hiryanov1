import asyncio


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f"{count=} секунд прошло")
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)

########################################################################################################
import requests
from time import time


def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r  # r - это обьект response


def write_file(response):
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)


def main1():
    t0 = time()
    url = r"https://loremflickr.com/320/240"
    for i in range(10):
        write_file(get_file(url))

    print(time() - t0)

###############################################################################################################
import  aiohttp  # Для асинхронных запросов

# Эта функция записи файлов - синхронная, но есть библиотеки для асинхронной записи в файл тоже
def write_image(data):
    filename = 'file-{}.jpeg'.format(time() * 1000)
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


async def main2():
    t0 = time()
    url = r"https://loremflickr.com/320/240"
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)
        await asyncio.gather(*tasks)

    print(time() - t0)


if __name__ == '__main__':
    #asyncio.run(main())  # Асинхронность вывода
    #main1()  # Синхронные запросы в сеть
    #asyncio.run(main2())  # Асинхронные запросы в сеть # такой вызов работает, но показывает ошибки

    loop = asyncio.get_event_loop()  # Такой вызов без ошибок
    loop.run_until_complete(main2())