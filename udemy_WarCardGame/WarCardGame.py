import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
# ranks tuple is added to be sure rank name in the ranks and rank name in the
# values match to each other.

ranks = ('Two', 'Three', 'Four', 'Five','Six', 'Seven','Eight','Nine','Ten', 'Jack',
         'Queen','King','Ace')

values = {'Two':2, 'Three':3, 'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,
          'Ten':10,'Jack':11,'Queen':12, 'King':13,'Ace':14}

class Card:
    #Suit is type of card such as Heart, Diamond etc.
    #Rank is the rank of the card(Written on the card)
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    #Print the suit and value
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                #Create the Card Object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

