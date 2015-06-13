# card.py
# ===*===
# by Annie Leonard
# This module should create a card with a randomly generated suit and rank.

class Card:
    "A card represents a playing card"
    import random

    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, card_rank, card_suit):
        self.card_rank = random.choice(ranks)
        self.card_suit = random.choice(suits)
    def __repr__(self):
        return "This card is a {} of {}".format(self.card_rank, self.card_suits)
playing_card = Card(card_rank, card_suit)
