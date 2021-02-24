def decor(func):
    def wrapper():
        func()

    return wrapper


@decor  # Это декоратор, в нем мало смысла
def show():
    print("hello")


show()