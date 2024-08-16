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
    def flip(self):
        self.face_up = not self.face_up
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def draw(self, offset_x=0, offset_y=0):
        x = self.x+offset_x
        y = self.y+offset_y
        sc = Screen.get()
        cls = type(self)
        sc.draw(x, y, cls.image)
        if self.face_up:
            text = self.symbol+self.number
            sc.draw(x+1, y+1, text)
            sc.draw(x+cls.width-1-len(text), y+3, text)
        else:
            sc.draw(x+1, y+1, " ,, \n || \n '' ")
                


