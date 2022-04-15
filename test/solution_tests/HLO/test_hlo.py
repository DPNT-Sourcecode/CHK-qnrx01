import unittest
import solutions.HLO.hello_solution as hello_solution


class HelloTestCase(unittest.TestCase):
    def test_hello_george(self):
        res = hello_solution.hello("George")
        self.assertEqual(res, "Hello George")  # add assertion here


if __name__ == '__main__':
    unittest.main()

