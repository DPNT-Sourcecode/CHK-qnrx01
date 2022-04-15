import itertools


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    return Checkout().get_price(skus)


class Product:
    def __init__(self, price, offer_qty=0, offer_price=0, offer2_qty=0, offer2_price=0):
        self.price = price
        self.offer_qty = offer_qty
        self.offer_price = offer_price
        self.offer2_qty = offer2_qty
        self.offer2_price = offer2_price

    def get_price(self, qty):
        if self.offer_qty == 0:
            return self.price * qty
        elif self.offer2_qty == 0:
            offers = qty // self.offer_qty
            normal = qty % self.offer_qty
            return self.offer_price * offers + self.price * normal
        else:
            offers2 = qty // self.offer2_qty
            remainder = qty % self.offer2_qty
            offers = remainder // self.offer_qty
            normal = remainder % self.offer_qty
            return self.offer2_price * offers2 + self.offer_price * offers + self.price * normal


class SpecialOffer:
    def __init__(self, product, qty, second_product):
        self.product = product
        self.qty = qty
        self.second_product = second_product
        self.discount = 2

    def get_discount(self, product_list, products):
        ct = list(product_list).count(self.product)
        offers = ct // self.qty
        second_product_ct = list(product_list).count(self.product)
        discount_qty = min(offers, second_product_ct)
        return -1 * products[self.second_product].get_price(discount_qty)


class Checkout:
    def __init__(self):
        self.price_list = {'A':(50, 3, 130, 5, 200), 'B':(30,2,45),'C':(20,0,0),'D':(15,0,0),'E':(40,0,0)}
        self.products = { k:Product(*v) for k, v in self.price_list.items() }

    def get_price(self, product_list: str):
        price = 0
        for product in set(product_list):
            if product not in self.products:
                return -1
            cnt = list(product_list).count(product)
            price += self.products[product].get_price(cnt)
        specials = [SpecialOffer('E', 2, 'B')]
        for special in specials:
            price += special.get_discount(product_list, self.products)
        return price


check = Checkout()
check.get_price("EEB")

