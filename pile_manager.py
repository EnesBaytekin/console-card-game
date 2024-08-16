from controller import Controller
from time import time
from screen import Screen
from utils import is_colliding

class PileManager:
    def __init__(self, **piles):
        self.piles = piles
        self.selection = list(piles.keys())[0]
        self.mode = "piles"
        self.colliding_piles = []
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
    def previous(self):
        names = list(self.piles.keys())
        index = names.index(self.selection)
        name = names[(index-1)%len(names)]
        self.select(name)
        pile = self.get_current()
        self.remove_pile(name)
        self.add_pile(name, pile)
    def draw(self):
        sc = Screen.get()
        for name, pile in self.piles.items():
            pile.draw()
            if self.mode == "piles":
                if name == self.selection:
                    sc.draw(pile.x, pile.y, "#@@@@#\n\n\n\n#@@@@#")
                    sc.draw(0, sc.height-1, f"size: {pile.size()}")
            elif self.mode == "cards":
                if name == self.selection:
                    current = self.get_current()
                    sc.draw(pile.x, pile.y, "o@@@@o\n\n\n\no@@@@o")
                    card = current.cards[current.index]
                    sc.draw(pile.x+card.x, pile.y+card.y, "c@@@@c\n\n\n\nc@@@@c")
            elif self.mode == "select_pile":
                for i, pile in enumerate(self.colliding_piles):
                    c = chr(65+i)
                    sc.draw(pile.x, pile.y, f"{c}@@@@{c}\n\n\n\n{c}@@@@{c}")
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
            if con.check("t"):
                piles = []
                for pile in self.piles.values():
                    if pile is current:
                        continue
                    if is_colliding(current.get_rect(), pile.get_rect()):
                        piles.append(pile)
                if len(piles):
                    self.colliding_piles = piles
                    self.mode = "select_pile"
            if con.check("e"):
                self.next()
            if con.check("E"):
                self.previous()
            if con.check("r"):
                self.mode = "cards"
        elif self.mode == "cards":
            current.update()
            if con.check("r"):
                self.mode = "piles"
        elif self.mode == "select_pile":
            if len(self.colliding_piles) == 1:
                selected_pile = self.colliding_piles[0]
            else:
                selected_pile = None
                for i, pile in enumerate(self.colliding_piles):
                    if con.check(chr(65+i), chr(97+i)):
                        selected_pile = pile
                        break
            if selected_pile is not None:
                current.assemble(selected_pile)
                index = list(self.piles.values()).index(selected_pile)
                name = list(self.piles.keys())[index]
                self.remove_pile(self.selection)
                self.select(name)
                self.remove_pile(name)
                self.add_pile(name, selected_pile)
                self.mode = "piles"

