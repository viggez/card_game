from random import shuffle
from card_game import Card


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ('Hearts', 'Diamonds', 'Clubs', 'Spades'):
            for rank in range(2, 15):
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    def __str__(self):
        return ', '.join([str(card) for card in self.cards])
