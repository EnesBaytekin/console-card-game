from card import Card
from screen import Screen
from controller import Controller
from os import get_terminal_size
from time import sleep
from pile import Pile
from pile_manager import PileManager

def main():
    sc = Screen.get()
    sc.init(50, 20, " ")
    con = Controller.get()
    cards = [
        Card(symbol, number, 1, 1, False)
        for symbol in "♣♦♥♠" for number in [*"A23456789", "10", *"JQK"]
    ]
    pile = Pile(2, 3, cards)
    pm = PileManager(
        deck=pile
    )
    while True:
        sleep(0.033)
        con.update()
        if con.check("q"):
            break
        pm.update()
        sc.clear()
        pm.draw()
        sc.set_at(sc.width-1, sc.height-1, ".")
        sc.update()

if __name__ == "__main__":
    main()

