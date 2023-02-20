from package_item_package.item_module import Item

class ShoppingCart:

    def __init__(self):
        self.type_item1 = None
        self.type_item2 = None

item1 = Item()
item2 = Item()

item1.id= "T1"
item1.descr = "Table1"
item1.price = 50
item1.quantity = 2

item2.id= "T2"
item2.descr = "Table2"
item2.price = 100
item2.quantity = 4

print(item1.descr)
print(item2.descr)

item1.discounted_price()
item2.discounted_price()



