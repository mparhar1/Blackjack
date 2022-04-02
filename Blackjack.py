# Game: BLACKJACK (a.k.a. Twenty-One)

# Imports
import random

# Card Deck
suits = ("Clubs", "Spades", "Hearts", "Diamonds")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" : 7, "Eight" : 8, "Nine" : 9, "Ten" : 10, "Jack" : 10,
          "Queen" : 10, "King" : 10, "Ace" : 11}

# Symbolic Global Variable
playing = True

class Card:
    # Creates a Card With the Suit & Rank
    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit

    # Returns the Card's Information as a Print String
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    # Creates the Deck
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    # Creates the Deck with the Print Strings
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()

     # Deals Out a Card from the Deck
    def deal(self):
        single_card = self.deck.pop()
        return single_card

    # Shuffles Deck
    def shuffle(self):
        random.shuffle(self.deck)

class Hand:
    # Creates the Player's Hand
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    # Adds a card to Player's Hand
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    # If Player Busts, but has an Ace,
    # lowers the Ace's value from 11 to 1
    def ace_adjustment(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Give a "hit"
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.ace_adjustment()

# Asks Player for their Decision & Executes
def hit_stand_decision(deck, hand):
    global playing
    while True:
        decision = input("\nDo you want to Hit or Stand (Enter: 'Hit' or 'Stand')? ")
        if decision.lower() == "hit":
            hit(deck, hand)
        elif decision.lower() == "stand":
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Invalid response, please try again...")
            continue
        break

# Displays Table Cards With One of the Dealer's Cards Face Down
def reveal_some(player, dealer):
    print("\nDealer's Hand:")
    print("", dealer.cards[1])
    print(" <card hidden>")
    print("\nPlayer's Hand:", *player.cards, sep="\n ")

# Display All Table Cards
def reveal_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)

# End-of-Game Scenarios
# Player Busts
def player_busts(player, dealer):
    print("\nPLAYER BUSTS! THE DEALER WINS!\n")

# Dealer Busts
def dealer_busts(player, dealer):
    print("\nDEALER BUSTS! THE PLAYER WINS!\n")

# Player Has the Higher Hand
def player_higher(player, dealer):
    print("\nPLAYER WINS WITH THE HIGHER HAND!\n")

# Dealer Has the Higher Hand
def dealer_higher(player, dealer):
    print("\nDEALER WINS WITH THE HIGHER HAND!\n")

# Player & Dealer Push (Tie)
def push(player, dealer):
    print("\nHANDS ARE EQUAL! IT'S A PUSH!\n")

# Game Logic
while True:
    # Welcome Statement
    print("Welcome to BLACKJACK!")
          
    # Rules
    print("\nRULES:\n1) Closest hand to 21 without going over wins!\n2) All face cards are worth 10\n3) Dealer will hit until they reach 17\n4) Aces count as 1 or 11")
    # Prepare Deck
    deck = Deck()
    deck.shuffle()

    # Create Player's Hand
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    # Create Dealer's Hand
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Reveal the Hands with One of the Dealer's Cards Hidden
    reveal_some(player_hand, dealer_hand)

    while playing:
        # Ask & Execute Player's Decision
        hit_stand_decision(deck, player_hand)

        # Show the Updated Table
        reveal_some(player_hand, dealer_hand)

        # Check if Player Busts
        if player_hand.value > 21:
            player_hand.ace_adjustment()
            player_busts(player_hand,dealer_hand)
            break

    # Execute Dealer's Hand Until Hand Value <=17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Reveal Dealer's Final Hand
        reveal_all(player_hand, dealer_hand)

        # Check for End-of-Game Scenarios
        if dealer_hand.value > 21:
            dealer_hand.ace_adjustment()
            dealer_busts(player_hand,dealer_hand,)
        elif dealer_hand.value < player_hand.value:
            player_higher(player_hand, dealer_hand)
        elif dealer_hand.value > player_hand.value:
            dealer_higher(player_hand, dealer_hand)
        else:
            push(player_hand, dealer_hand)

    # Ask if Player Wants to Play Again
    new_game = input("Would you like to play another hand (Enter 'Yes' or 'No')? ")
    if new_game.lower() == "yes":
        playing = True
        continue
    else:
        # Closing Message
        print("\nThanks for playing!")
        break
