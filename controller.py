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
        if self.buffer == []: return
        while True:
            if self._replace("\x1b[A", "up"): continue
            if self._replace("\x1b[B", "down"): continue
            if self._replace("\x1b[C", "right"): continue
            if self._replace("\x1b[D", "left"): continue
            if self._replace("\x1b[Z", "shift+tab"): continue
            if self._replace("\x1b", "esc"): continue
            if self._replace("\t", "tab"): continue
            if self._replace("\n", "enter"): continue
            break
    def _replace(self, old, new):
        i = self._index(old)
        if i is not None:
            for _ in range(len(old)):
                self.buffer.pop(i)
            self.buffer.insert(i, new)
            return True
        return False
    def _index(self, target):
        target = list(target)
        start = 0
        index = 0
        for i, c in enumerate(self.buffer):
            if target[index] == c:
                if index == 0:
                    start = i
                if index == len(target)-1:
                    return start
                index += 1
            else:
                index = 0
        return None

if __name__ == "__main__":
    from time import sleep
    con = Controller.get()
    while True:
        sleep(0.2)
        con.update()
        if len(con.buffer):
            print("\t", con.buffer)

