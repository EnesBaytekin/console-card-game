from controller import Controller

class Pile:
    def __init__(self, x, y, cards=[]):
        self.x = x
        self.y = y
        self.cards = []
        for card in cards:
            self.add_card(card)
        self.index = 0
    def add_card(self, card):
        card.x = 0
        card.y = 0
        self.cards.append(card)
    def remove_card(self, card):
        self.cards.remove(card)
        card.x += self.x
        card.y += self.y
        if self.index >= len(self.cards):
            self.index -= 1
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def draw(self):
        for card in self.cards:
            card.draw(self.x, self.y)
    def split(self, number=1):
        cards = self.cards[-number:]
        top_card = cards[-1]
        pile = Pile(self.x+top_card.x, self.y+top_card.y)
        for card in cards:
            self.remove_card(card)
            pile.add_card(card)
        return pile
    def flip(self):
        for card in self.cards:
            card.flip()
        self.cards = self.cards[::-1]
    def size(self):
        return len(self.cards)
    def update(self):
        con = Controller.get()
        dx = con.check("d")-con.check("a")
        dy = con.check("s")-con.check("w")
        card = self.cards[self.index]
        card.move(dx, dy)
        if con.check("e"):
            self.index = (self.index+1)%len(self.cards)
        if con.check("E"):
            self.index = (self.index-1)%len(self.cards)

