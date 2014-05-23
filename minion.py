class Minion(object):
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
