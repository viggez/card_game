class Card:
    """Represents a standard playing card."""

    def __init__(self, rank, suit):
        """Initialize a new card with the given suit and value."""
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """Return a human-readable string representation of the card."""
        rank_str = str(self.rank)
        if self.rank == 11:
            rank_str = "Jack"
        elif self.rank == 12:
            rank_str = "Queen"
        elif self.rank == 13:
            rank_str = "King"
        elif self.rank == 14:
            rank_str = "Ace"
        return f"{rank_str} of {self.suit}"

    def get_value(self):
        """Get the numerical value of the card's rank."""
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
        """Compare two cards for less-than based on their values."""
        return self.get_value() < other.get_value()

    def __gt__(self, other):
        """Compare two cards for greater-than based on their values."""
        return self.get_value() > other.get_value()

    def __eq__(self, other):
        """Compare two cards for equality based on their values."""
        return self.get_value() == other.get_value()
