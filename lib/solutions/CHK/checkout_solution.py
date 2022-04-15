import itertools


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    return Checkout().get_price(skus)


class Product:
    def __init__(self, price, offer_qty=0, offer_price=0):
        self.price = price
        self.offer_qty = offer_qty
        self.offer_price = offer_price

    def get_price(self, qty):
        if self.offer_qty == 0:
            return self.price * qty
        else:
            offers = qty // self.offer_qty
            normal = qty % self.offer_qty
            return self.offer_price * offers + self.price * normal


class Checkout:
    def __init__(self):
        self.price_list = { 'A':(50,3,130), 'B':(30,2,45),'C':(20,0,0),'D':(15,0,0),'E':(40,3,80)}
        self.products = { k:Product(*v) for k, v in self.price_list.items() }

    def get_price(self, product_list: str):
        price = 0
        for product in set(product_list):
            if product not in self.products:
                return -1
            cnt = list(product_list).count(product)
            price += self.products[product].get_price(cnt)
        return price




