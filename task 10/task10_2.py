class Hotdogs:

    def __init__(self, name, sausages, price, rating):
        self.name = name
        self.sausages = sausages     # number of sausages inside
        self.price = price
        self.rating = rating      # how many points out of 10


single = Hotdogs('Одинарный', 1, 51, 9)
double = Hotdogs('Двойной', 2, 64, 8)
triple = Hotdogs('Тройной', 3, 76, 6)
master = Hotdogs('Мастерский с сарделькой', 1, 89, 8)
