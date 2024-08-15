from controller import Controller

class PileManager:
    def __init__(self, **piles):
        self.piles = piles
        self.selection = list(piles.keys())[0]
    def get_current(self):
        return self.piles[self.selection]
    def select(self, name):
        self.selection = name
    def draw(self):
        for pile in self.piles.values():
            pile.draw()
    def update(self):
        con = Controller.get()
        dx = con.check("d")-con.check("a")
        dy = con.check("s")-con.check("w")
        current = self.get_current()
        current.move(dx, dy)

