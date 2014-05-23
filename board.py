
import minion_list
import character

class Board(object):
    """The game board"""

    def __init__(self):
        self.my_side = minion_list.MinionList()
        self.their_side = minion_list.MinionList()

    def summon_minion(self, card_proto, position, side):
        side.insert(character.Minion(card_proto), position)

    def get_my_side(self):
        """My sides!"""
        return self.my_side

    def get_their_side(self):
        return self.their_side

    def get_sides(self):
        return iter((self.my_side, self.their_side))

    def get_number_of_minions(self):
        return len(self.my_side) + len(self.their_side)


