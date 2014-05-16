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
