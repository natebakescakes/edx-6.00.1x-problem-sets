class Queue(object):
    def __init__(self):
        self.vals = []
    
    def insert(self, other):
        self.vals.append(other)
        
    def remove(self):
        if len(self.vals) == 0:
            raise ValueError()
        else:
            return self.vals.pop(0)