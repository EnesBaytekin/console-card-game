from os import system, get_terminal_size

class Screen:
    instance = None
    @classmethod
    def get(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance
    def init(self, width, height, bg="."):
        self.width = width
        self.height = height
        self.bg = bg
        self.buffer = [[self.bg for _ in range(height)] for _ in range(width)]
        self.changed = False
    def fill(self, c):
        self.buffer = [[c for _ in range(self.height)] for _ in range(self.width)]
        self.changed = True
    def clear(self):
        self.fill(self.bg)
    def set_at(self, x, y, c):
        if 0<=x<self.width and 0<=y<self.height:
            self.buffer[x][y] = c
            self.changed = True
    def get_at(self, x, y):
        return self.buffer[x][y]
    def draw(self, x, y, string, colorkey="@"):
        lines = string.split("\n")
        width = max([len(line) for line in lines])
        height = len(lines)
        for dx in range(width):
            for dy in range(height):
                try:
                    c = lines[dy][dx]
                except IndexError:
                    c = colorkey
                if c != colorkey:
                    if 0<=x+dx<self.width and 0<=y+dy<self.height:
                        self.set_at(x+dx, y+dy, c)
    def update(self):
        if self.changed:
            system("clear")
            for y in range(self.height):
                for x in range(self.width):
                    print(self.get_at(x, y), end="")
                print()
            self.changed = False
        width, height = get_terminal_size()
        if width != self.width or height != self.height:
            self.init(width, height, self.bg)

