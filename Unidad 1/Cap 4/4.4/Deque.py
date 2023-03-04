class Deque(object):
    def __init__(self, size):
        self.items = [None] * size
        self.primer = 0
        self.ultimo = 0
        self.size = size
        
    def insertLeft(self, item):
        if self.isFull():
            self.resize1(2 * self.size)  # Duplica el tamaño de la deque
        self.primer = (self.primer - 1) % self.size
        self.items[self.primer] = item
    
    def insertRight(self, item):
        if self.isFull():
            self.resize1(2 * self.size)  # Duplica el tamaño de la deque
        self.items[self.ultimo] = item
        self.ultimo = (self.ultimo + 1) % self.size
    
    def resize1(self, new_size):
        old_items = self.items
        self.items = [None] * new_size
        for i in range(self.size):
            self.items[i] = old_items[(self.primer + i) % self.size]
        self.primer = 0
        self.ultimo = self.size
        self.size = new_size


    def removeLeft(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        item = self.items[self.primer]
        self.items[self.primer] = None
        self.primer = (self.primer + 1) % self.size
        return item
    
    def removeRight(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        self.ultimo = (self.ultimo - 1) % self.size
        item = self.items[self.ultimo]
        self.items[self.ultimo] = None
        return item

    def peekLeft(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        return self.items[self.primer]

    def peekRight(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        return self.items[self.ultimo - 1]

    def isEmpty(self):
        return self.primer == self.ultimo and self.items[self.primer] is None

    def isFull(self):
        return self.primer == self.ultimo and self.items[self.primer] is not None
    
    def printDeque(self):
        if self.isEmpty():
            print('Deque vacía')
        else:
            print('Contenido de la deque:')
            i = self.primer
            while i != self.ultimo:
                print(self.items[i], end=' ')
                i = (i + 1) % self.size
            print()