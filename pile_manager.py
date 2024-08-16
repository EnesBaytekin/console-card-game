from controller import Controller
from time import time
from screen import Screen

class PileManager:
    def __init__(self, **piles):
        self.piles = piles
        self.selection = list(piles.keys())[0]
        self.mode = "piles"
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
        pile = self.get_current()
        self.remove_pile(name)
        self.add_pile(name, pile)
    def draw(self):
        sc = Screen.get()
        for name, pile in self.piles.items():
            pile.draw()
            if name == self.selection:
                if self.mode == "piles":
                    sc.draw(pile.x, pile.y, "#@@@@#\n\n\n\n#@@@@#")
                elif self.mode == "cards":
                    current = self.get_current()
                    sc.draw(pile.x, pile.y, "o@@@@o\n\n\n\no@@@@o")
                    card = current.cards[current.index]
                    if card.x != 0 or card.y != 0:
                        sc.draw(pile.x+card.x, pile.y+card.y, "c@@@@c\n\n\n\nc@@@@c")
    def update(self):
        con = Controller.get()
        current = self.get_current()
        if self.mode == "piles":
            dx = con.check("d")-con.check("a")
            dy = con.check("s")-con.check("w")
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
            if con.check("r"):
                self.mode = "cards"
        elif self.mode == "cards":
            current.update()
            if con.check("r"):
                self.mode = "piles"

