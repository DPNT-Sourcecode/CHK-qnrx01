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
        assert check.get_price("AABBCCDDEE") == 100 + 30 + 40 + 30 + 80

    def test_checkout5(self):
        check = checkout_solution.Checkout()
        assert check.get_price("AABBCCDDEEE") == 100 + 30 + 40 + 30 + 120

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

    def test_checkout10(self):
        check = checkout_solution.Checkout()
        assert check.get_price("ABCDEABCDE") == 100 + 30 + 40 + 30 + 80

    def test_checkout11(self):
        check = checkout_solution.Checkout()
        assert check.get_price("FF") == 20

    def test_checkout12(self):
        check = checkout_solution.Checkout()
        assert check.get_price("FFF") == 20

    def test_checkout13(self):
        check = checkout_solution.Checkout()
        assert check.get_price("FFFF") == 30

    def test_checkout14(self):
        check = checkout_solution.Checkout()
        assert check.get_price("FFFFFF") == 40

    def test_checkout15(self):
        check = checkout_solution.Checkout()
        assert check.get_price("FFFFFF") == 40

    def test_checkout16(self):
        check = checkout_solution.Checkout()
        assert check.get_price("STXYZ") == 45 + 17 + 20

    def test_checkout17(self):
        check = checkout_solution.Checkout()
        assert check.get_price("SSTXYZ") == 90

    def test_checkout18(self):
        check = checkout_solution.Checkout()
        assert check.get_price("STY") == 45

    def test_checkout19(self):
        check = checkout_solution.Checkout()
        assert check.get_price("ZZZXX") == 45 + 17 + 17

   def

class TestBadInput:
    def test_bad_input(self):
        check = checkout_solution.Checkout()
        assert check.get_price("AAAaAcBBBCCD") == -1

class TestCheckoutCall:
    def test_checkout_call(self):
        assert checkout_solution.checkout("AAAABBBCCD") == 180 + 75 + 40 + 15
