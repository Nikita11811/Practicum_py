class Cleaner:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.access_level = 1
        self.id = id

    def info(self):
        print(self.name, self.age)

    def get_access_level(self):
        print('Access level is', self.access_level)

    def where_to_find(self):
        if self.id in (1, 9):
            room = 101
        elif self.id in (10, 20):
            room = 102
        else:
            room = 103
        print(f'Find cleaner in room {room}')


class Worker(Cleaner):
    def __init__(self, name, age, id):
        super().__init__(name, age, id)
        self.access_level = 2

    def info(self):
        print(self.name, self.age)

    def get_access_level(self):
        print('Access level is', self.access_level)

    def where_to_find(self):
        if self.id in (1, 9):
            room = self.id*5 + 100
        elif self.id in (10, 20):
            room = self.id*6 + 100
        else:
            room = 100 + self.id*3
        print(f'Find worker in room {room}')


class Manager(Worker):
    def __init__(self, name, age, id):
        super().__init__(name, age, id)
        self.access_level = 3

    def info(self):
        print(self.name, self.age)

    def get_access_level(self):
        print('Access level is', self.access_level)

    def where_to_find(self):
        if self.id in (1, 3):
            room = 201
            print(f'Find manager in room {room}')
        elif self.id in (3, 5):
            room = 202
            print(f'Find manager in room {room}')
        else:
            print('No idea where to find :(')


class Boss(Manager):
    def __init__(self, name, age, id):
        super().__init__(name, age, id)
        self.access_level = 4

    def info(self):
        print(self.name, self.age)

    def get_access_level(self):
        print('Access level is', self.access_level)

    def where_to_find(self):
        print('You do not need to find Boss - only He can find you')


Max = Manager('Max', '23', 34)
Max.get_access_level()
Max.info()
Max.where_to_find()
print('-------------------------')

Zoe = Cleaner('Zoe', 23, 2)
Zoe.get_access_level()
Zoe.info()
Zoe.where_to_find()
print('-------------------------')


Artem = Worker('Artem', 15, 9)
Artem.info()
Artem.where_to_find()
print('-------------------------')

Stas = Boss('STAS', 66, 1)
Stas.where_to_find()
print('-------------------------')
