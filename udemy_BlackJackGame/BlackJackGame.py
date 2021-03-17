import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True
# It starts playing. When False Game is over.

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suits

class Deck():
    def __init__(self):
        self.deck = [] # All 52 cards possibilities will go in deck list.
        for suit in suits:
            for rank in ranks:
                # Nested card list is created for every possible card variation.
                # Card variations are appended in deck list such as ((Heart, two))
                # (Ace, three) , (Diamond, four))
                self.deck.append(Class(suit, rank))

