from screen import Screen

class Card:
    image = """
.----.
|    |
|    |
|    |
'----'
    """.strip()
    width = 6
    height = 5
    def __init__(self, symbol, number, x=0, y=0, face_up=True):
        self.symbol = symbol
        self.number = number
        self.x = x
        self.y = y
        self.face_up = face_up
    def draw(self):
        sc = Screen.get()
        cls = type(self)
        sc.draw(self.x, self.y, cls.image)
        if self.face_up:
            text = self.symbol+self.number
            sc.draw(self.x+1, self.y+1, text)
            sc.draw(self.x+cls.width-1-len(text), self.y+3, text)
        else:
            sc.draw(self.x+1, self.y+1, " ,, \n || \n '' ")
                


