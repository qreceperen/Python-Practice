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
        return self.rank + ' of ' + self.suit

class Deck():
    def __init__(self):
        self.deck = [] # All 52 cards possibilities will go in deck list.
        for suit in suits:
            for rank in ranks:
                # Nested card list is created for every possible card variation.
                # Card variations are appended in deck list such as ((Heart, two))
                # (Ace, three) , (Diamond, four))
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: "+deck_comp
        # all possible cards are written as string for user to see.(string method)


    def shuffle(self):
        random.shuffle(self.deck) # Appended desk list is shuffled.

    def deal(self):
        single_card = self.deck.pop()
        return single_card
        # from appended deck list, one card is taken (pop will take the first card
        # by default, since the deck is shuffled before deal function first card
        # always will be different.
class Hand():
    # Hand class represents the cards in player's hand.
    def __init__(self):
        self.cards = []
        self.value = 0
        # Tracks the value of the cards that player holding.
        self.aces = 0
        # Aces can be 1 or 11 (Their value is dynamic)

    def add_card(self,card):
        # This function will add a card from deck to player's hand.
        self.cards.append(card)
        # Card attribute comes from deck class not from Card class.
        # from Deck.deal()--> single Card(suit,rank)
        self.value += values[card.rank]
        # self.value will increase according to card that delivered to player.
        # card.rank (it becomes key in values dictionary) will be checked from
        # values dictionary. From dictionary integer (rank) will be assigned to card
        # in order to make mathematical comparisons between players card values.


test_deck = Deck()
test_deck.shuffle()

# PLAYER
test_player = Hand()
# Deal 1 card from the deck CARD (suit, rank)
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)




























