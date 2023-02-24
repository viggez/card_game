class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def get_value(self):
        if self.rank == 'Jack':
            return 11
        elif self.rank == 'Queen':
            return 12
        elif self.rank == 'King':
            return 13
        elif self.rank == 'Ace':
            return 14
        else:
            return int(self.rank)

    def __lt__(self, other):
        return self.get_value() < other.get_value()

    def __gt__(self, other):
        return self.get_value() > other.get_value()

    def __eq__(self, other):
        return self.get_value() == other.get_value()
