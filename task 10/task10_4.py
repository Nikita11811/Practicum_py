class Human:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.tickets = []

    def buy_ticket(self, boxoffice, dest):
        boxoffice.sell_ticket(self, dest)

    def search_tickets(self, boxoffice):
        print('There are next tickets available at the box office:')
        boxoffice.show_tickets()
        print()

    def tickets_bought(self):
        print(self.name, 'has tickets to', str(self.tickets), '.')
        print()


class BoxOffice:

    def __init__(self, location):
        self.location = location
        self.tickets = {
            'Moscow': 3600,
            'Minsk': 5800,
            'Tomsk': 3200,
            'Omsk': 1800,
            'Berdsk': 60,
        }

    def show_tickets(self):
        for dest, price in self.tickets.items():
            print(dest, '\t', str(price))

    def sell_ticket(self, human, dest):
        if dest in self.tickets:
            price = self.tickets.get(dest)
            if human.balance >= price:
                human.balance -= price
                human.tickets.append(dest)
                print('You have bought a ticket to', dest, '.')
                print('You have', str(human.balance), 'rubles left.')
                print()
            else:
                print('Sorry,', human.name, ',your balance (', str(human.balance),
                      'rub ) is too low to buy this one (', dest, ').')
                print('Look at available tickets:')
                self.show_tickets()
                print()
        else:
            print('Sorry,', human.name, ',no tickets to', dest, 'available.')
            print('Please, look at available tickets:')
            self.show_tickets()
            print()


human1 = Human('Stas', 1000)
boxOffice = BoxOffice('Novosibirsk')

human1.search_tickets(boxOffice)

human1.buy_ticket(boxOffice, 'Moscow')
human1.buy_ticket(boxOffice, 'Samara')
human1.buy_ticket(boxOffice, 'Berdsk')

human1.tickets_bought()
