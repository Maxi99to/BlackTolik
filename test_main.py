import unittest
from main import add, multiply

class TestMathFunctions(unittest.TestCase):
    # Тест 1: сложение положительных чисел
    def test_add_positive(self):
        self.assertEqual(add(3, 7), 10)

    # Тест 2: умножение на ноль
    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)

if __name__ == '__main__':
    unittest.main()
