import unittest
from app.card import Card
from app.deck import Deck


class TestDeck(unittest.TestCase):
    """Test cases for the Deck class."""

    def test_create_deck(self):
        """Test if a Deck object is created with the correct number of cards."""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_contains_all_cards(self):
        """Test if the Deck object contains all the standard playing cards."""
        deck = Deck()
        for suit in ("Hearts", "Diamonds", "Clubs", "Spades"):
            for rank in range(2, 15):
                card = Card(rank, suit)
                self.assertIn(card, deck.cards)

    def test_shuffle_deck(self):
        """Test if the shuffle method shuffles the Deck object."""
        deck = Deck()
        original_order = list(deck.cards)
        deck.shuffle()
        self.assertNotEqual(deck.cards, original_order)

    def test_draw_card(self):
        """Test if the draw_card method returns a Card object and removes it from the Deck."""
        deck = Deck()
        card = deck.draw_card()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(deck.cards), 51)

    def test_draw_card_empty_deck(self):
        """Test the draw_card method when the Deck is empty."""
        deck = Deck()
        for _ in range(52):
            deck.draw_card()
        self.assertEqual(len(deck.cards), 0)
        card = deck.draw_card()
        self.assertIsNone(card)

    def test_deck_str(self):
        """Test the string representation of a Deck object."""
        deck = Deck()
        deck_str = str(deck)
        self.assertIsInstance(deck_str, str)


if __name__ == "__main__":
    unittest.main()
