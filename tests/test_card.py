import unittest
from app.card import Card


class TestCard(unittest.TestCase):

    def test_create_card(self):
        card = Card(2, "Hearts")
        self.assertEqual(card.rank, 2)
        self.assertEqual(card.suit, "Hearts")

    def test_card_str(self):
        card = Card(2, "Hearts")
        self.assertEqual(str(card), "2 of Hearts")
        card = Card(11, "Spades")
        self.assertEqual(str(card), "Jack of Spades")

    def test_get_value(self):
        card = Card(10, "Diamonds")
        self.assertEqual(card.get_value(), 10)
        card = Card(11, "Clubs")
        self.assertEqual(card.get_value(), 11)

    def test_comparisons(self):
        card1 = Card(2, "Hearts")
        card2 = Card(3, "Hearts")
        card3 = Card(3, "Diamonds")

        self.assertTrue(card1 < card2)
        self.assertTrue(card2 > card1)
        self.assertTrue(card2 == card3)


if __name__ == '__main__':
    unittest.main()
