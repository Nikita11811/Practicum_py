class Figure:
    def __init__(self, length, width, angles):
        self.length = length
        self.width = width
        self.angles = angles
        self.color = 'white'

    def change_color(self, color):
        self.color = color
        print('The figure is', self.color)

    def show_param(self):
        if self.angles == 1:
            print('You have a', self.color, 'simple angle:')
        elif self.angles == 2:
            print('You have a', self.color, 'δύογωνιἀ:')
        elif self.angles == 3:
            print('You have a', self.color, 'triangle:')
        elif self.angles == 4:
            if self.length == self.width:
                print('You have a', self.color, 'square:')
            else:
                print('You have a', self.color, 'quadrangle:')
        else:
            print('You have something weird with', self.angles, 'angles:')


class Square(Figure):
    def __init__(self, length, width, angles):
        super().__init__(length, width, angles)
        if self.angles != 4:
            print('It is not a square...')

    def show_param(self):
        print(f"You have a {self.color} square with Length = {self.length} and Width = {self.width}")


class Oval(Figure):
    def __init__(self, length, width, angles):
        super().__init__(length, width, angles)
        if self.angles != 0:
            print('An oval cannot have angles...')

    def show_param(self):
        print(f"You have an {self.color} oval with Big axis = {self.length} and Small axis = {self.width}")


tr = Figure(2, 3, 4)
#tr.change_color('black')
#tr.show_param()
s1 = Square(2, 3, 4)
s1.show_param()
o1 = Oval(5, 4, 0)
o1.show_param()
