import solutions.HLO.hello_solution as hello_solution


class TestSum:
    def test_hello_john(self):
        res = hello_solution.hello("John")
        assert res == "Hello, John!"



