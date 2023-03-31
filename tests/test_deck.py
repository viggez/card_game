import unittest
from app.card import Card
from app.deck import Deck


class TestDeck(unittest.TestCase):

    def test_create_deck(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_contains_all_cards(self):
        deck = Deck()
        for suit in ('Hearts', 'Diamonds', 'Clubs', 'Spades'):
            for rank in range(2, 15):
                card = Card(rank, suit)
                self.assertIn(card, deck.cards)

    def test_shuffle_deck(self):
        deck = Deck()
        original_order = list(deck.cards)
        deck.shuffle()
        self.assertNotEqual(deck.cards, original_order)

    def test_draw_card(self):
        deck = Deck()
        card = deck.draw_card()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(deck.cards), 51)

    def test_draw_card_empty_deck(self):
        deck = Deck()
        for _ in range(52):
            deck.draw_card()
        self.assertEqual(len(deck.cards), 0)
        card = deck.draw_card()
        self.assertIsNone(card)

    def test_deck_str(self):
        deck = Deck()
        deck_str = str(deck)
        self.assertIsInstance(deck_str, str)


if __name__ == '__main__':
    unittest.main()
