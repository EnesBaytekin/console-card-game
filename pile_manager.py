from controller import Controller
from time import time

class PileManager:
    def __init__(self, **piles):
        self.piles = piles
        self.selection = list(piles.keys())[0]
    def add_pile(self, name, pile):
        self.piles[name] = pile
    def remove_pile(self, name):
        del self.piles[name]
    def get_current(self):
        return self.piles[self.selection]
    def select(self, name):
        self.selection = name
    def next(self):
        names = list(self.piles.keys())
        index = names.index(self.selection)
        name = names[(index+1)%len(names)]
        self.select(name)
    def draw(self):
        for pile in self.piles.values():
            pile.draw()
    def update(self):
        con = Controller.get()
        dx = con.check("d")-con.check("a")
        dy = con.check("s")-con.check("w")
        current = self.get_current()
        current.move(dx, dy)
        if con.check(" "):
            pile = current.split(1)
            pile.flip()
            if current.size() == 0:
                self.remove_pile(self.selection)
            else:
                pile.move(0, 1)
            name = f"{self.selection}.{time()}"
            self.add_pile(name, pile)
            self.select(name)
        if con.check("e"):
            self.next()

