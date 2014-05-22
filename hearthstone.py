from enum import Enum

class Card(object):
    """Common data across all cards"""
    class Rarity(Enum):
        Free = 1
        Common = 2
        Rare = 3
        Epic = 4
        Legendary = 5
        
    class Class(Enum):
        Any = 1
        Druid = 2
        Hunter = 3
        Mage = 4
        Paladin = 5
        Priest = 6
        Rogue = 7
        Shaman = 8
        Warlock = 9
        Warrior = 10
        
    def __init__(self, mana_cost, name, card_class=Class.Any, rarity=None, flavour_text=None, is_golden=False):
        self.mana_cost = mana_cost
        self.name = name
        self.card_class = card_class
        self.rarity = rarity
        self.flavour_text = flavour_text
        self.is_golden = is_golden
    
    def get_mana_cost(self):
        return self._mana_cost
        
    def get_name(self):
        return self.name
        
    def get_rarity(self):
        return self.rarity
        
    def get_flavour_text(self):
        return self.flavour_text
    
    def get_class(self):
        """The class that this card belongs to (Druid, Mage, etc)"""
        return self.card_class
        
    def is_golden(self):
        """Not planned for use but included to complete the model"""
        return self.is_golden
        
class MinionCard(Card):
    """
    Represents the prototype data for a Minion.
    When a Minion is summoned, its initial data is loaded from a 
    MinionCard.
    """
    class Race(Enum):
        General = 1
        Beast = 2
        Demon = 3
        Dragon = 4
        Murloc = 5
        Pirate = 6
        Totem = 7
        
    def __init__(self, mana_cost, name, attack, health, card_class=Card.Class.Any, race=Race.General, rarity=None, flavour_text=None):
        super().__init__(mana_cost, name, card_class, rarity, flavour_text)
        self.attack = attack
        self.health = health
        self.race = race
        
    @classmethod
    def make(cls, iterable):
        """For loading from JSON/DB"""
        return cls(*iterable)
    
    def get_attack(self):
        return self.attack
        
    def get_health(self):
        return self.health
        
    def get_race(self):
        return self.race

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
    
class MinionList(object):
    """LinkedList of minions, represents a side of the field"""
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def __getitem__(self, position):
        current = self._head
        i = 0
        while i < position:
            if current == None:
                raise IndexError()
            current = current.get_right()
            i += 1
        return current
        
    def __iter__(self):
        current = self._head
        while current != None:
            yield current
            current = current.get_right()
            
    def __reversed__(self):
        current = self._tail
        while current != None:
            yield current
            current = current.get_left()
        
    def insert(self, position, minion):
        if position > self._size or position < 0:
            raise IndexError()
        if position == self._size:
            self._tail = minion
            if self._size == 0:
                self._head = minion
            else:
                node = self[self._size - 1]
                minion._set_left(node)
                node._set_right(minion)
        else:
            node = self[position]
            minion._set_left(node.get_left())
            node._set_left(minion)
            minion._set_right(node)
            if minion.get_left():
                minion.get_left()._set_right(minion)
            if position == 0:
                self._head = minion
        self._size += 1
        
    def remove(self, minion):
        left = minion.get_left()
        right = minion.get_right()
        
        if left:
            left._set_right(right)
        else:
            self._head = right
            
        if right:
            right._set_left(left)
        else:
            self._tail = left

        self._size -= 1
        
    def index(self, minion):
        for i, m in enumerate(self):
            if m == minion:
                return i
        raise ValueError('Not in the list')
            
    def push_right(self, minion):
        self.insert(len(self), minion)
    
    def push_left(self, minion):
        self.insert(0, minion)
               
class Board(object):
    """The game board"""
    def __init__(self):
        pass
        
    def summon_minion(self, card_proto, position):
        pass