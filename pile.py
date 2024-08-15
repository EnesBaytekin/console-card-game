

class Pile:
    def __init__(self, x, y, cards):
        self.x = x
        self.y = y
        self.cards = []
        for card in cards:
            self.add_card(card)
    def add_card(self, card):
        card.x = 0
        card.y = 0
        self.cards.append(card)
    def remove_card(self, card):
        self.cards.remove(card)
        card.x += self.x
        card.y += self.y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def draw(self):
        for card in self.cards:
            card.draw(self.x, self.y)

