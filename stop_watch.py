def increment(self):
    self.s.increment()
    if self.s.value == 0:
        self.m.increment()
        if self.m.value == 0:
            self.h.increment()


def decr(self):
    self.s.decr()
    if self.s.value == self.s.max:
        self.m.decr()
        if self.m.value == self.m.max:
            self.h.decr()

"""
seq branch: t prop to N 
bim search: t prop to logN

tomp = 100ns
N = 10 undo


    
"""
