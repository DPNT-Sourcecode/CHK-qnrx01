

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    raise NotImplementedError()


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

