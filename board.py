import minion_list
import character

class Board(object):
    """The game board"""

    def __init__(self):
        self._my_side = minion_list.MinionList()
        self._their_side = minion_list.MinionList()

    def summon_minion(self, card_proto, position, side):
        side.insert(position, character.Minion(card_proto))

    def get_my_side(self):
        """My sides!"""
        return self._my_side

    def get_their_side(self):
        return self._their_side

    def get_sides(self):
        return iter((self._my_side, self._their_side))

    def get_number_of_minions(self):
        return len(self._my_side) + len(self._their_side)


