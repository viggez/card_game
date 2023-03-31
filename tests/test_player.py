import unittest
from app.card import Card
from app.player import Player


class TestPlayer(unittest.TestCase):

    def test_create_player(self):
        player = Player("Alice")
        self.assertEqual(player.name, "Alice")
        self.assertEqual(player.hand, [])

    def test_add_card(self):
        player = Player("Alice")
        card = Card(2, "Hearts")
        player.add_card(card)
        self.assertEqual(player.hand, [card])

    def test_remove_card(self):
        player = Player("Alice")
        card = Card(2, "Hearts")
        player.add_card(card)
        removed_card = player.remove_card()
        self.assertEqual(removed_card, card)
        self.assertEqual(player.hand, [])

    def test_play_card(self):
        player = Player("Alice")
        card = Card(2, "Hearts")
        player.add_card(card)
        played_card = player.play_card()
        self.assertEqual(played_card, card)
        self.assertEqual(player.hand, [])

    def test_play_card_empty_hand(self):
        player = Player("Alice")
        played_card = player.play_card()
        self.assertIsNone(played_card)

    def test_clear_hand(self):
        player = Player("Alice")
        card = Card(2, "Hearts")
        player.add_card(card)
        player.clear_hand()
        self.assertEqual(player.hand, [])

    def test_player_str(self):
        player = Player("Alice")
        card = Card(2, "Hearts")
        player.add_card(card)
        player_str = str(player)
        self.assertEqual(player_str, "Alice has 1 cards")


if __name__ == '__main__':
    unittest.main()
