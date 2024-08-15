from tty import setraw
from termios import tcgetattr, tcsetattr, TCSADRAIN
from sys import stdin
from os import O_NONBLOCK
from fcntl import fcntl, F_GETFL, F_SETFL

def get_character():
    fd = stdin.fileno()
    old_settings = tcgetattr(fd)
    old_flags = fcntl(fd, F_GETFL)
    try:
        setraw(fd)
        fcntl(fd, F_SETFL, old_flags | O_NONBLOCK)
        byte = stdin.buffer.raw.read(1)
        if byte is not None:
            return byte.decode()
        else:
            return None
    finally:
        fcntl(fd, F_SETFL, old_flags)
        tcsetattr(fd, TCSADRAIN, old_settings)

class Controller:
    instance = None
    @classmethod
    def get(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance
    def __init__(self):
        self.buffer = []
    def check(self, char):
        return char in self.buffer
    def update(self):
        self.buffer.clear()
        while True:
            c = get_character()
            if c is None:
                break
            else:
                self.buffer.append(c)

