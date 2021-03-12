import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
# ranks tuple is added to be sure rank name in the ranks and rank name in the
# values match to each other.

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
         'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    # Suit is type of card such as Heart, Diamond etc.
    # Rank is the rank of the card(Written on the card)
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    # Print the suit and value
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        # shuffle the card list internally it shuffles the all_cars list
        random.shuffle(self.all_cards)

    def deal_one(self):
        # grabbing one of the card in the list. Remove one card from the
        # all_card list and use it whenever need it.
        return self.all_cards.pop()


class Player:
    # This class hold a player's current list of cards.
    def __init__(self, name):
        # name is for player name
        # all card refers the card that player holds.
        self.name = name
        self.all_cards = []

    def remove_one(self):
        # this function is going to remove a card from player decks.
        # Card is going to be removed from the top of the deck
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # add_card function is going to add card to players deck when player win cards.
        # Cards will be added to the bottom of the player's deck.
        if type(new_cards) == type([]):
            # During the waw situation multiple cards might be gained. In this type of
            # situation extend method will combine the card deck with player's deck.
            self.all_cards.extend(new_cards)
        else:
            # if player gains only one card.
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# GAME SETUP
# players are created from player class. Game is played with two player.
player_one = Player("One")
player_two = Player('Two')

# players cards are created and shuffled.
new_deck = Deck()
new_deck.shuffle()

# There are 52 cards in the deck that's why range is 26 (half of 52) in order to divide
# into two evenly. Both players have 26 cards.
# 26 Cards are added to both players according to Deck class deal_one function.
for x in range(26):
    # add_cards, divided cards (26) added to player one and player two
    # add_cards function needs an argument. new_deck.deal_one is the argument given.
    # This argument is called from Deck classes deal one function. It removes a card from
    # players' deck(from top). In other words, player puts a card on the table from his deck.

    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# START THE GAME
game_on = True
# game on is added like that because we will use while loop.

# while game on
round_num = 0  # we will count the rounds.
while game_on:
    round_num += 1
    print(f'Round {round_num}')

    # Check one of the player is out of cards or not. Because if any player out of cards
    # while loop should stop and one of the player wins the game.
    if len (player_one.all_cards) == 0:
        print(f'Player One, out of cards! Player two wins')
        game_on = False
        break

    if len (player_two.all_cards) == 0:
        print(f'Player Two, out of cards! Player one wins')
        game_on = False
        break

    # START A NEW ROUND
    player_one_cards = []
    # This is the card player one leave on the table to start playing.
    player_one_cards.append(player_one.remove_one())
    # A card will be removed from top of player's deck and appended in player_one_cards
    # list in order to compare player_one_cards and player two cards.

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    # Same steps above is repeated for the player two.

    # WHILE AT WAR
















































