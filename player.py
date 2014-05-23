class GamePlayer(object):
    """Represents a player in the game"""

    def __init__(self, deck, hero):
        self._initial_deck = deck
        self._deck = list(deck)
        self._hero = hero
        self._hand = []
        self._max_mana = 0
        self._mana = 0

    def get_hero(self):
        """The Character representing the Player's Hero"""
        return self._hero

    def get_initial_deck(self):
        return self._initial_deck

    def get_deck(self):
        return self._deck
        
    def get_hand(self):
        return self._hand

    def add_to_hand(self, card):
        """Adds a card to the Player's Hand"""
        self._hand.append(card)

    def play_card(self, index):
        """Plays a card from the Player's Hand"""
        card = self._hand.pop(index)
        # TODO

    def get_max_mana(self):
        return self._max_mana

    def set_max_mana(self, amount):
        self._max_mana = amount

    def increment_max_mana(self):
        """Purely for convenience and readability"""
        self.set_max_mana(self.get_max_mana() + 1)

    def get_mana(self):
        return self._mana

    def set_mana(self, amount):
        self._mana = amount

    def refill_mana(self):
        self.set_mana(self.get_max_mana())
        # TODO Overload