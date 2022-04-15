import solutions.HLO.hello_solution as hello_solution


class TestSum:
    def test_hello_george(self):
        res = hello_solution.hello("George")
        assert res == "Hello George"


