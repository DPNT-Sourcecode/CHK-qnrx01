import solutions.CHK.checkout_solution as checkout_solution


class TestProduct:
    def test_standard_price(self):
        prod = checkout_solution.Product(100)
        assert prod.get_price(4) == 400

    def test_offer_exact(self):
        prod = checkout_solution.Product(100, 3, 200)
        assert prod.get_price(3) == 200

    def test_offer_extra(self):
        prod = checkout_solution.Product(100, 3, 200)
        assert prod.get_price(4) == 300

    def test_offer_unused(self):
        prod = checkout_solution.Product(100, 3, 200)
        assert prod.get_price(1) == 100


class TestCheckout:
    def test_checkout1(self):
        check = checkout_solution.Checkout()
        assert check.get_price("AAAABBBCCD") == 180 + 75 + 40 + 15

    def test_checkout2(self):
        check = checkout_solution.Checkout()
        assert check.get_price("ABCD") == 50 + 30 + 20 + 15

    def test_checkout3(self):
        check = checkout_solution.Checkout()
        assert check.get_price("ABCDABCD") == 215

    def test_checkout4(self):
        check = checkout_solution.Checkout()
        assert check.get_price("ABCDABCDEE") == 215 + 80 - 30

    def test_checkout5(self):
        check = checkout_solution.Checkout()
        assert check.get_price("ABCDABCDEEE") == 215 + 120 - 30

    def test_checkout6(self):
        check = checkout_solution.Checkout()
        assert check.get_price("AAAAAAAAA") == 200 + 130 + 50

    def test_checkout7(self):
        check = checkout_solution.Checkout()
        assert check.get_price("EEB") == 80

    def test_checkout8(self):
        check = checkout_solution.Checkout()
        assert check.get_price("EEEB") == 120

    def test_checkout9(self):
        check = checkout_solution.Checkout()
        assert check.get_price("EE") == 80

    def test_checkout9(self):
        check = checkout_solution.Checkout()
        assert check.get_price("ABCDEABCDE") == 100 + 45 + 


class TestBadInput:
    def test_bad_input(self):
        check = checkout_solution.Checkout()
        assert check.get_price("AAAaAcBBBCCD") == -1

class TestCheckoutCall:
    def test_checkout_call(self):
        assert checkout_solution.checkout("AAAABBBCCD") == 180 + 75 + 40 + 15





