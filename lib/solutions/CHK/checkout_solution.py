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


class SpecialOfferFree:
    def __init__(self, product, qty, second_product):
        self.product = product
        self.qty = qty
        self.second_product = second_product
        self.discount = 2

    def remove_free_products(self, product_list, products):
        ct = product_list.count(self.product)
        offers = ct // self.qty
        for _ in range(offers):
            if self.second_product in product_list:
                product_list.remove(self.second_product)
        return product_list


class GroupDiscount:
    def __init__(self,qty = 3,price = 45, group_buy=["S","T","X","Y","Z"]):
        self.group_buy = group_buy
        self.qty = qty
        self.price = price
        self.total_price = 0

    def remove_offer_products(self, product_list, products):
        sorted_product_list = sorted(product_list, key=lambda x: products[x].price)[::-1]
        ct = sum(1 for v in sorted_product_list if v in self.group_buy)
        offers = ct // self.qty
        for _ in range(3*offers):
            for v in sorted_product_list:
                if v in sorted_product_list:
                    sorted_product_list.remove(v)
                    break
        self.total_price = offers * 45
        return sorted_product_list

    def get_group_price(self):
        return self.total_price


class Checkout:
    def __init__(self):
        self.price_list = {'A': (50, 3, 130, 5, 200), 'B': (30, 2, 45), 'C': (20, 0, 0), 'D': (15, 0, 0),
                           'E': (40, 0, 0), 'F': (10, 3, 20), 'G': (20, 0, 0), 'H': (10, 5, 45, 10, 80),
                           'I': (35, 0, 0), 'J': (60, 0, 0), 'K': (70, 2, 120), 'L': (90, 0, 0), 'M': (15, 0, 0),
                           'N': (40, 0, 0), 'O': (10, 0, 0), 'P': (50, 5, 200), 'Q': (30, 3, 80), 'R': (50, 0, 0),
                           'S': (20, 0, 0), 'T': (20, 0, 0), 'U': (40, 4, 120), 'V': (50, 2, 90, 3, 130),
                           'W': (20, 0, 0), 'X': (17, 0, 0), 'Y': (20, 0, 0), 'Z': (21, 0, 0)}
        self.products = { k:Product(*v) for k, v in self.price_list.items() }

    def get_price(self, product_list: str):
        product_list = list(product_list)
        price = 0
        for product in set(product_list):
            if product not in self.products:
                return -1
        specials = [SpecialOfferFree(*x) for x in [('E', 2, 'B'), ('N', 3, 'M'), ('R', 3, 'Q')]]
        for special in specials:
            product_list = special.remove_free_products(product_list, self.products)
        gd = GroupDiscount()
        product_list = gd.remove_offer_products(product_list, self.products)
        for product in set(product_list):
            cnt = product_list.count(product)
            price += self.products[product].get_price(cnt)
        return price + gd.get_group_price()


check = Checkout()
check.get_price("STXYZ")






