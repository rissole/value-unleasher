class Character(object):
    """Abstract class. Character must be either a Minion or a Hero"""

    def __init__(self, card_proto): 
        self._card_proto = card_proto

    def get_health(self):
        raise NotImplementedError("Character must be either a Minion or a Hero")

    def get_attack(self):
        raise NotImplementedError("Character must be either a Minion or a Hero")

    def get_card_prototype(self):
        return self._card_proto


class Minion(Character):
    """Represents a Minion on the Board"""

    def __init__(self, card_proto):
        super().__init__(card_proto)
        self._left = None
        self._right = None
        
    def get_health(self):
        return self._card_proto.get_health()

    def get_attack(self):
        return self._card_proto.get_attack()

    def get_left(self):
        """Get the Minion to the left"""
        return self._left

    def get_right(self):
        """Get the Minion to the right"""
        return self._right

    def _set_left(self, minion):
        self._left = minion

    def _set_right(self, minion):
        self._right = minion


class Hero(Character):
    """Hero represents the Player's character"""

    def __init__(self, card_proto=None):
        super().__init__(card_proto)

    def get_health(self):
        return self._card_proto.get_health()

    def get_attack(self):
        #TODO Weapons
        return 0


