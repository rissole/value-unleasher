class Character(object):

    def __init__(self): 
        raise NotImplemented("Um no.")

    def get_health(self):
        raise NotImplemented("Um no.")

    def get_attack(self):
        raise NotImplemented("Um no.")

    def get_card_prototype(self):
        return self._card_proto


class Minion(Character):
    """Represents a Minion on the Board"""
    def __init__(self, card_proto):
        self._card_proto = card_proto
        self._left = None
        self._right = None

    def get_card_prototype(self):
        return self._card_proto

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

    def __init__(self, minion_card_proto=None):
        # The proto needs to be of an actual minion.
        self.card_proto = minion_card_proto

    def get_health(self):
        return self.card_proto.get_health()

    def get_attack(self):
        """TODO Weapons"""
        return 0


