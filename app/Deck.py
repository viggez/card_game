from random import shuffle
from app.card import Card


class Deck:
    """Represents a standard deck of playing cards."""

    def __init__(self):
        """Initialize a new deck of 52 playing cards."""
        self.cards = []
        for suit in ('Hearts', 'Diamonds', 'Clubs', 'Spades'):
            for rank in range(2, 15):
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        """Shuffle the deck of cards."""
        shuffle(self.cards)

    def draw_card(self):
        """Draw a card from the top of the deck."""
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    def __str__(self):
        return ', '.join([str(card) for card in self.cards])
