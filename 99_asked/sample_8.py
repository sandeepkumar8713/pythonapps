# Coupon Template:
# Give X% discount on all item.
# Give P% discount on the next item.
# Give Y$ discount for Nth product of specific type.
# Example:
# Cart 1:
# 10% discount on the next item.
# A notebook of 10$.
# A t-shirt of 20$
# Cart price : (10-10*.1) + 20 = 29
#
# Cart 2:
# A notebook of 10$.
# 10% discount on the next item.
# A t-shirt of 20$
# Cart price : 10 + (20-20*.1) = 28
#
# Cart 3:
# A notebook of 10$.
# 10% discount on all item.
# 5% discount on next item.
# 2$ off on 2nd Notebook.
# A notebook of 10$
# Cart Price: (10 - 1) + (10- 1 - .45 -2) = 9+ 6.55 = 15.55
#
# Note:
# Product & Discount both can be added to the cart.
# Entire cart information is passed to the service/library in one go.
# It’s entirely in memory processing, taking the cart information and returning the final price.
# We are not looking for any UI or API designing
# .
# LLD : come up with the entities, what their properties and behavior are. How are the entities associated (Is-A/has-A).
# Write the function which will calculate the final price.
# Pick a programming language and editor of your choice.
# Ignore setter , getter , constructor.
# You can write the entire code in a single file , easy to understand for the interview process.

from abc import ABC
import enum


class Item(ABC):
    def getPrice(self):
        raise NotImplemented


class Product(Item):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getPrice(self):
        return self.price

class Discount(Item):
    def getDiscount(self):
        raise NotImplemented

class PercentageDiscount(Discount):
    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def getDiscount(self, price):
        return (price * self.discount_percentage) / 100.0

class AllDiscount(PercentageDiscount):
    pass

class NextDiscount(PercentageDiscount):
    pass


class NthDiscount(Discount):
    def __init__(self, nth_item, discount_amount):
        self.nth_item = nth_item
        self.discount_amount = discount_amount


class ShoppingCart():
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def get_final_price(self):
        if len(self.items) == 0:
            return 0

        discounts = []
        products = []
        for item in self.items:
            if isinstance(item, Product):
                products.append(item)
            else:
                discounts.append(item)

        if len(products) == 0:
            return 0

        discount_pointer = 0
        product_pointer = 0
        total = 0
        while discount_pointer < len(discounts) and product_pointer < len(products):
            this_product_price = products[product_pointer].getPrice()
            this_discount = discounts[discount_pointer]

            total += this_product_price
            if isinstance(this_discount, PercentageDiscount):
                discount = this_discount.getDiscount(this_product_price)
                total -= discount



class ItemType(enum):
    PRODUCT = 'PRODUCT'
    ALLDISCOUNT = 'ALLDISCOUNT'
    NEXTDISCOUNT = 'NEXTDISCOUNT'
    NTHDISCOUNT = 'NTHDISCOUNT'


class ItemFactory:
    @staticmethod
    def create_object(itemType, itemName= None, itemPrice= None, discountPercentage= None, nthDiscountItem = None, nthDiscount = None):
        if itemType == ItemType.PRODUCT:
            return Product(itemName, itemPrice)
        elif itemType == ItemType.ALLDISCOUNT:
            return AllDiscount(discountPercentage)
        elif itemType == ItemType.NEXTDISCOUNT:
            return NextDiscount(discountPercentage)
        elif itemType == ItemType.NthDiscount:
            return NthDiscount(nthDiscountItem, nthDiscount)

        return None


def driver_function():
    shoppingCart = ShoppingCart()

    # 10% discount on the next item.
    # # A notebook of 10$.
    # # A t-shirt of 20$

    item_1 = ItemFactory.create_object(
        itemType=ItemType.NEXTDISCOUNT,
        discountPercentage=10.0
    )
    item_2 = ItemFactory.create_object(
        itemType=ItemType.PRODUCT,
        itemName="Notebook",
        itemPrice=10
    )
    item_3 = ItemFactory.create_object(
        itemType=ItemType.PRODUCT,
        itemName="T-shirt",
        itemPrice=20
    )

    shoppingCart.addItem(item_1)
    shoppingCart.addItem(item_2)
    shoppingCart.addItem(item_3)
    total_price = shoppingCart.get_final_price()
