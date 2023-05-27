class Crocodile:

    def __init__(self, name):
        self.name = name
        self.__age = 16
        self.__favourite_food = 'meeeeaaaaat'

    def show_info(self):
        print(self.__age, 'years old crocodile', self.name, 'greets you! Look at him!')
        self.__make_happy('meat')

    def set_age(self, age):
        if 0 < age < 40:
            self.__age = age
        else:
            print("Crocodile can not have this age!")

    def get_age(self):
        return self.__age

    def get_favourite_food(self):
        return self.__favourite_food

    def __make_happy(self, food):
        if food == self.__favourite_food:
            print('Crocodile is happy!')
        else:
            print("Crocodile isn't happy")

    def set_favourite_food(self, food):
        if type(food) == str:
            self.__favourite_food = food
        else:
            print("It's not a food")


crocodile_1 = Crocodile('Simon')
crocodile_1.show_info()
crocodile_2 = Crocodile('Billy')
crocodile_2.set_age(38)
crocodile_2.set_favourite_food(5)
crocodile_2.set_favourite_food('meat')
crocodile_2.show_info()

print("\nLet's make the first crocodile happy too!")
crocodile_1.set_favourite_food('meat')
crocodile_1.show_info()
