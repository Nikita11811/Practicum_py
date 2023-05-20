class Cat:
    def __init__(self, catsname, is_hungry):
        self.catsname = catsname
        self.is_hungry = is_hungry


class Human:
    def __init__(self, humansname, catsname):
        self.humansname = humansname
        self.catsname = catsname

    def feed(self, cat: Cat):
        if cat.is_hungry:
            cat.is_hungry = False


Mars = Cat('Mars', True)
Mark = Human('Mark', 'Mars')
print('8 am: Is the Cat hungry? ', Mars.is_hungry)
Mark.feed(Mars)
print('9 am: Is the Cat hungry? ', Mars.is_hungry)
