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
        raise ValueError('Minion %s not found.' % (minion,))
            
    def push_right(self, minion):
        self.insert(len(self), minion)
    
    def push_left(self, minion):
        self.insert(0, minion)
               
