class Box:
    def __init__(self):
        self.figures = []

    def put_in(self, figure):
        self.figures.append(figure)

    def desc(self):
        print(f"There are next figures in the box:")
        for figure in self.figures:
            figure.desc()


class Figure:
    name = None

    def __init__(self, color):
        self.color = color
        self.box = None

    def desc(self):
        print(f"A {self.color} {self.name}")


class Square(Figure):
    name = "square"

    def __init__(self, color, length):
        self.a = length
        super().__init__(color)


class Circle(Figure):
    name = "circle"

    def __init__(self, color, radius):
        self.r = radius
        super().__init__(color)


class Triangle(Figure):
    name = "triangle"

    def __init__(self, color, a, b, cos):
        self.a = a
        self.b = b
        self.cos = cos
        super().__init__(color)


box_1 = Box()

figure_1 = Square("gold", 8)
figure_2 = Circle("white", 3)
figure_3 = Triangle("multicolor", 15, 2, 60)

box_1.put_in(figure_1)
box_1.put_in(figure_2)
box_1.put_in(figure_3)

box_1.desc()
