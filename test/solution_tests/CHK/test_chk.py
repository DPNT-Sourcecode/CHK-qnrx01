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