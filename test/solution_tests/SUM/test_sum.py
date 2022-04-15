from solutions.SUM import sum_solution


class TestSum:
    def test_one_plus_two(self):
        assert sum_solution.compute(1, 2) == 3

    def test_three_plus_two(self):
        assert sum_solution.compute(3, 2) == 5

    def test_minus_one_plus_two(self):
        assert sum_solution.compute(-1, 2) == 1




