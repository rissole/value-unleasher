import hearthstone
import unittest

class TestMinionList(unittest.TestCase):

    def setUp(self):
        self.minionA = hearthstone.Minion('A')
        self.minionB = hearthstone.Minion('B')
        self.minionC = hearthstone.Minion('C')
        
    def test_len(self):
        l = hearthstone.MinionList()
        self.assertEqual(0, len(l))
        l.push_right(self.minionA)
        self.assertEqual(1, len(l))
        l.push_left(self.minionB)
        self.assertEqual(2, len(l))
        
    def test_iter(self):
        l = hearthstone.MinionList()
        l.push_right(self.minionA)
        l.push_right(self.minionB)
        l.push_right(self.minionC)
        order = [m.get_card_prototype() for m in l]
        self.assertEqual(['A', 'B', 'C'], order)
        
    def test_reversed_iter(self):
        l = hearthstone.MinionList()
        l.push_right(self.minionA)
        l.push_right(self.minionB)
        order = [m.get_card_prototype() for m in reversed(l)]
        self.assertEqual(['B', 'A'], order)
        l.push_left(self.minionC)
        order = [m.get_card_prototype() for m in reversed(l)]
        self.assertEqual(['B', 'A', 'C'], order)
        
    def test_push_left(self):
        l = hearthstone.MinionList()
        l.push_left(self.minionA)
        l.push_left(self.minionB)
        l.push_right(self.minionC)
        order = [m.get_card_prototype() for m in l]
        self.assertEqual(['B', 'A', 'C'], order)
        
    def test_insert(self):
        l = hearthstone.MinionList()
        l.push_right(self.minionA)
        l.push_right(self.minionB)
        # A B
        #0 1 2
        l.insert(1, self.minionC)
        order = [m.get_card_prototype() for m in l]
        self.assertEqual(['A', 'C', 'B'], order)
        
    def test_empty(self):
        l = hearthstone.MinionList()
        self.assertEqual(0, len(l))
        order = [m.get_card_prototype() for m in l]
        self.assertEqual(0, len(order))
        order = [m.get_card_prototype() for m in reversed(l)]
        self.assertEqual(0, len(order))
        
    def test_remove(self):
        l = hearthstone.MinionList()
        l.push_right(self.minionA)
        l.push_right(self.minionB)
        l.push_right(self.minionC)
        l.remove(self.minionB)
        order = [m.get_card_prototype() for m in l]
        self.assertEqual(['A', 'C'], order)
        l.push_left(self.minionB)
        l.remove(self.minionB)
        order = [m.get_card_prototype() for m in l]
        self.assertEqual(['A', 'C'], order)
    
if __name__ == '__main__':
    unittest.main()