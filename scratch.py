'''
How to play

Welcome to Blackjack! This guide shall walk you through the basics of the game and get you ready to hit the tables with confidence. 

Objective
The main objective is to obtain a hand with a total value higher than the dealer's without going over 21.

Players
The game involves at least two players, the Dealer and Player. In this Blackjack game you, Player, will play against the dealer. 

The game uses the standard 52-card deck. Each player will be handed two cards each; yours will be face-up but only one of the Dealer's will be shown. Each turn after, you will be given the option to keep the cards (stay) or get more (draw) depending on their current total. Remember, don't go over 21!

*Hint: The Dealer is programmed to keep drawing as long as their current value is not yet over 16.


If your total hits exactly 21, congratulations that's a blackjack!

 

Step 2: Card Values

Before you dive into the action, familiarize yourself with the card values:

Number cards (2-10): Face value
Face cards (Jack, Queen, King): 10 points each
Ace: 1 or 11 points (whichever benefits you more)
Step 3: The Deal

You receive two cards, both face-up. The dealer also gets two cards, but one is face-down (the hole card). This adds an element of mystery and strategy to the game.

Step 4: Aim for 21, but Don't Go Over!

Your goal is to get a hand value as close to 21 as possible without exceeding it. If you go over 21, you bust and lose the round. But if you hit 21 exactly with your first two cards, congratulations – you've got a blackjack and win extra!
'''

import random

class BlackjackGame:
    def __init__(self):
        self.deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        self.player_hand = set()
        self.dealer_hand = set()

    def deal_card(self, hand):
        card = random.choice(self.deck)
        hand.add(card)
        self.deck.remove(card)

    def display_hands(self, show_all=False):
        print("Player's hand:", self.player_hand)
        
        if show_all:
            print("Dealer's hand:", self.dealer_hand)
        else:
            print("Dealer's hand: {hidden card}")

# Example usage:
game = BlackjackGame()

# Deal initial cards
game.deal_card(game.player_hand)
game.deal_card(game.dealer_hand)
game.deal_card(game.player_hand)
game.deal_card(game.dealer_hand)

# Display hands with hidden card
game.display_hands(show_all=False)
