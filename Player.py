

class Player:

    def __init__(self, name):
        self.player = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        self.hand.remove(card)

    def get_hand(self):
        return self.hand

    def clear_hand(self):
        self.hand = []

    def __str__(self):
        return f'{self.name} has {len(self.hand)} cards'
