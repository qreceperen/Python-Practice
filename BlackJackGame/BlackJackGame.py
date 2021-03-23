import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

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
        self.deck = []  # All 52 cards possibilities will go in deck list.
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
        return "The deck has: " + deck_comp
        # all possible cards are written as string for user to see.(string method)

    def shuffle(self):
        random.shuffle(self.deck)  # Appended desk list is shuffled.

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

    def add_card(self, card):
        # This function will add a card from deck to player's hand.
        self.cards.append(card)
        # Card attribute comes from deck class not from Card class.
        # from Deck.deal()--> single Card(suit,rank)
        self.value += values[card.rank]
        # self.value will increase according to card that delivered to player.
        # card.rank (it becomes key in values dictionary) will be checked from
        # values dictionary. From dictionary integer (rank) will be assigned to card
        # in order to make mathematical comparisons between players card values.

        # track aces
        if card.rank == 'Ace':
            self.aces += 1
        # this command identify is there aces in the player's hand or not
        # by increasing self.aces value

    def adjust_for_ace(self):
        # If total value > 21 and still have an ace than change my ace to be 1 instead of 11
        while self.value > 21 and self.ace > 0:
            self.value -= 10
            self.aces -= 1
            # Ace value in the values dictionary is 11 by default. According to
            # game rule ace can be 11 or 1. If players card value is more than 21
            # ace should be 1, else ace should be 11. (self.value -=10 , 11-10 =1 ace
            # value becomes 1 if self.value >21)
            # self.aces decreased by one after using ace value.


class Chips:
    # You can think chips as money gaining and losing process
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        # Add to total money according to player's bet.

    def lose_bet(self):
        self.total -= self.bet
        # Subtract from total according to player's bet.


# Start writing functions to start the game.
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips! You have: {}".format(chips.total))
            # Amount of chips cannot overdue the total.( Total represent amount of money player holds.


def hit(deck, hand):
    single_card = deck.deal()
    # It takes single card from deck.(From deck class)
    hand.add_cards(single_card)
    # Evaluates the card value and add the card to player's hand.
    hand.adjust_for_ace()
    # Make arrangement if the card is Ace (Consider card value as 1 or 11)


def hit_or_stand(deck, hand):
    # This function ask player to continue taking card or stop taking card.
    # Player will take card with hit function. According to value of the card
    # player should decide whether continue taking card or stop taking card.
    # Hit or stand function provide taking card or stop taking card.

    global playing  # to control an upcoming while loop
    while True:
        x = input("Hit or stand? Enter h or s")

        if x[0].lower() == 'h':
            # if player write Capital we convert to lower letter to evaluate correctly.
            # if player write more than one character (like "Stand" etc.. we take only first character by x[0].
            hit(deck, hand)
            # Player will continue taking card from deck. (From hit function)

        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False
            # Player stands ( stop taking cards and game stops. )
        else:
            print("Sorry, I did not understand that, Please enter h or s only!")
            continue
            # If player write something that not starting with s or h loop will
            # continue until player writes something starting with s or h.
        break

def show_some(player,dealer):
    '''According to game playing dealer and player take two cards at the beginning.
    Both player open second card and both see the card value. Second card is closed
    (only dealers second card is closed) Player does not see the dealer's second
    card at the beginning'''

    # Show some function allow us to see dealer's second card. First card remain
    # hidden. ([0] first position, [1] is second position.)
    print ("\n Dealer's Hand: ")
    print ("First card hidden!")
    print (dealer.cards[1])
    # It shows second card.(Dealer's first card is dealer.cards[0] is hidden

    # Show all (2 cards) of player's hand cards.
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    # Basically player see both his/her cards but does not see dealer's second card.
































