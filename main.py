from card import Card
from screen import Screen
from os import get_terminal_size

def main():
    sc = Screen.get()
    width, height = get_terminal_size()
    sc.init(width, height, " ")
    cards = [
        Card(symbol, number, 1, 1)
        for symbol in "♣♦♥♠" for number in [*"A23456789", "10", *"JQK"]
    ]
    cards[9].x = 20
    cards[-2].x = 9
    cards[-1].x = 12
    cards[-1].y = 3
    sc.clear()
    for card in cards:
        card.draw()
    sc.update()

if __name__ == "__main__":
    main()

