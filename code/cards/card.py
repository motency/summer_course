# card.py
# ===*===
# by Annie Leonard

# Give a description of this module here...

class Card:
    "A card represents a playing card"
    from random import random

    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    short_suits = ["C", "D", "H", "S"]
    short_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, card_number):
        pass
    def __repr__(self):
        return "This card is a {} of {}".format(self.ranks, self.suits)


