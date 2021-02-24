import unittest


def fib(n):
    '''
    Число Фибоначчи
    :param n: неотрицательное число int
    :return: int
    '''
    if not isinstance(n, int):
        raise TypeError("Передан неверный тип, нужен int")
    if n < 0:
        raise ValueError("Число должно быть >=0")
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


class TestStringMethods(unittest.TestCase):

    def test_upper(self):  # имя фунции должно начинаться с test_, иначе не сработает
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())

    def test_fib_simple(self):
        for param, results in [(0, 0), (1, 1), (2, 1), (3, 2), (10, 55)]:
            self.assertEqual(fib(param), results)

    def test_fib_stress(self):
        with self.assertRaises(ValueError):
            fib(-1)
        with self.assertRaises(TypeError):
            fib(4.35345)


if __name__ == '__main__':
    unittest.main()  # Так запускаются тесты, сам метод main не нужен
            # Ctrl+Shift+F10



