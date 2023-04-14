import unittest
from app.card import Card
from app.player import Player


class TestPlayer(unittest.TestCase):
    """Test cases for the Player class."""

    def test_create_player(self):
        """Test if a player object is created correctly."""
        player = Player("Alice")
        self.assertEqual(player.name, "Alice")
        self.assertEqual(player.hand, [])

    def test_add_card(self):
        """Test if the add_card method adds a card to the player's hand."""
        player = Player("Alice")
        card = Card(2, "Hearts")
        player.add_card(card)
        self.assertEqual(player.hand, [card])

    def test_remove_card(self):
        """Test if the remove_card method removes a card from the player's hand."""
        player = Player("Alice")
        card = Card(2, "Hearts")
        player.add_card(card)
        removed_card = player.remove_card()
        self.assertEqual(removed_card, card)
        self.assertEqual(player.hand, [])

    def test_play_card(self):
        """Test if the play_card method plays a card from the player's hand."""
        player = Player("Alice")
        card = Card(2, "Hearts")
        player.add_card(card)
        played_card = player.play_card()
        self.assertEqual(played_card, card)
        self.assertEqual(player.hand, [])

    def test_play_card_empty_hand(self):
        """Test if the play_card method returns None when the player's hand is empty."""
        player = Player("Alice")
        played_card = player.play_card()
        self.assertIsNone(played_card)

    def test_clear_hand(self):
        """Test if the clear_hand method clears the player's hand."""
        player = Player("Alice")
        card = Card(2, "Hearts")
        player.add_card(card)
        player.clear_hand()
        self.assertEqual(player.hand, [])

    def test_player_str(self):
        """Test if the player's string representation is correct."""
        player = Player("Alice")
        card = Card(2, "Hearts")
        player.add_card(card)
        player_str = str(player)
        self.assertEqual(player_str, "Alice holds 1 cards")


if __name__ == "__main__":
    unittest.main()
