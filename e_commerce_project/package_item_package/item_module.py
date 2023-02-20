class Item:

    def __init__(self):
        self.id = None
        self.descr = None
        self.quantity = None
        self.price = None

    def discounted_price(self):
        if (self.quantity == 2):
            self.price = (self.price - (self.price * 10 / 100) * self.quantity)
            print(self.price)
        elif (self.quantity >=3 and self.quantity <= 5):
            self.price = (self.price - (self.price * 15 / 100) * self.quantity)
            print(self.price)
        elif (self.quantity >=5):
            self.price = (self.price - (self.price * 10 / 100) * self.quantity)
            print(self.price)
