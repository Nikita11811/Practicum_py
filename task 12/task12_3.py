class JellyBears:

    def __init__(self, brand, amount):
        self.brand = brand
        self.amount = amount

    def __purchase(self):
        print('Successfully!')

    def buy_bears(self):
        self.__purchase()
        print('You have bought', self.amount, 'packs of', self.brand, 'bears)')


purchase_1 = JellyBears('haribo', 8)
purchase_1.buy_bears()
