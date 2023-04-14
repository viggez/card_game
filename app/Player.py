class Player:
    """Represents a player in the card game."""

    def __init__(self, name):
        """Initialize a new player with the given name."""
        self.name = name
        self.hand = []

    def add_card(self, card):
        """Add a card to the player's hand."""
        self.hand.append(card)

    def remove_card(self):
        """Remove a card from the player's hand."""
        return self.hand.pop()

    def play_card(self):
        """Play a card from the player's hand."""
        if len(self.hand) == 0:
            return None
        return self.hand.pop(0)

    def gh(self):
        """Get the player's hand."""
        return self.hand

    def clear_hand(self):
        """Clear the player's hand."""
        self.hand = []

    def __str__(self):
        """Return a string representation of the player."""
        return f"{self.name} has {len(self.hand)} cards"
