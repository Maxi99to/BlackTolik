import unittest
from main import add, multiply
import logging

class TestMathFunctions(unittest.TestCase):
    def setUp(self):
        logging.info("Starting test execution")

    def tearDown(self):
        logging.info("Test execution completed")

    def test_add_positive(self):
        logging.info("Running test_add_positive")
        self.assertEqual(add(3, 7), 10)
        logging.info("test_add_positive passed")


    def test_multiply_by_zero(self):
        logging.info("Running test_multiply_by_zero")
        self.assertEqual(multiply(5, 0), 0)
        logging.info("test_multiply_by_zero passed")

    def test_add_negative(self):
        logging.info("Running test_add_negative")
        try:
            result = add(-3, -7)
            self.assertEqual(result, -10)
            logging.info("test_add_negative passed")
        except Exception as e:
            logging.error(f"test_add_negative failed: {str(e)}")
            raise

    def test_multiply_large_numbers(self):
        logging.info("Running test_multiply_large_numbers")
        self.assertEqual(multiply(1000, 2000), 2000000)
        logging.info("test_multiply_large_numbers passed")

    def test_error_handling(self):
        logging.info("Running test_error_handling")
        with self.assertRaises(TypeError):
            add("string", 5)
        logging.warning("test_error_handling: caught expected TypeError")

if __name__ == '__main__':
    unittest.main()
