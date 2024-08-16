from utils import get_character

class Controller:
    instance = None
    @classmethod
    def get(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance
    def __init__(self):
        self.buffer = []
    def check(self, *chars):
        for char in chars:
            if char in self.buffer:
                return True
        return False
    def update(self):
        self.buffer.clear()
        while True:
            c = get_character()
            if c is None:
                break
            else:
                self.buffer.append(c)

