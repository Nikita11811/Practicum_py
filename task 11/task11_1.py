class Table:
    def __init__(self, l, w, h):
        self.long = l
        self.width = w
        self.height = h

    def outing(self):
        print(self.long, self.width, self.height)


class Kitchen(Table):
    def howplaces(self, n):
        if n < 2:
            print("It is not kitchen table")
        else:
            self.places = n

    def outplases(self):
        print(self.places)


class Worker(Table):
    def square(self):
        print("The surface square is", self.long*self.width)

    def safety(self, plants):
        if plants > 0:
            print('The air is fresh enough!')
        else:
            print('You should have at least one plant!')


w1 = Worker(4, 2, 1)
w1.square()
w1.safety(3)
