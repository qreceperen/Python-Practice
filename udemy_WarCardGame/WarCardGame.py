class Card:
    #Suit is type of card such as Heart, Diamond etc.
    #Rank is the rank of the card(Written on the card)
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    #Print the suit and value
    def __str__(self):
        return self.rank + " of " + self.suit

two_hearts = Card('Hearts', 'Two')

print(two_hearts)
