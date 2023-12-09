import random
import os
from collections import deque
playerIn = True
dealerIn = True
playerHand = []
dealerHand = []

# iask kung kelangan tlg lambda!!
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.get_value()
        self.symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
        
    def __str__(self): # convert card object to str
        return (f"{self.rank}{self.symbols[self.suit]}")
    
    def get_value(self):
        if self.rank in ["J", "Q", "K"]:
            return 10
        elif self.rank == "A":
            return 11 
        else:
            return int(self.rank)

                
class Deck():
    def __init__(self):
        self.cards = [] #stack
        self.build()
    
    def build(self):
        ranks = ("A", "K", "Q", "J", "9", "8", "7", "6", "5", "4", "3", "2")
        suits = ("D", "C", "H", "S")
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def printDeck(self):
        cards=[]
        ranks = ("A", "K", "Q", "J", "9", "8", "7", "6", "5", "4", "3", "2")
        suits = ("D", "C", "H", "S")
        # 2d array
        for rank in ranks:
            one_rank = []
            for suit in suits:
                one_rank.append(Card(rank,suit))
            cards.append(one_rank)

        firstcard = True
        for suit in cards:
            for card in suit:
                if not firstcard:
                    print('\t', end='')
                print('\t', card, end="\t")
                firstcard = False
            print('\n')
            firstcard = True
  
             
    def shuffle(self):
        random.shuffle(self.cards)
        
    def drawCard(self):
        return self.cards.pop()
    
    def resetDeck(self):
        deck.build()

class Player:
    def __init__(self):
        self.hand = set()
        self.lives = self.lifeBar()
    
        
    def drawplayerCard(self, deck):
        card = random.choice(deck)
        self.hand.add(card)
        deck.remove(card)
    
    def totalHand(self):
        total = 0
        for card in self.hand:
            total += card.get_value()
            if card.rank == "A":
                if total > 21: # special condition ng ace
                    total -= 10
        return total
    
    def showHand(self):
        for card in self.hand:
            print(card)

    def resetHand(self):
        self.hand.clear()
        
    def lifeBar(self):
        return deque(['▓'] * 5)
        
    def decreaseLife(self):
        self.lives.pop() #queue implementation
    
    def resetLife(self):
        self.lives.clear()
        self.lives = self.lifeBar()
        
    
class Dealer():
    def __init__(self):
        self.hand = []
        
    def showDealerHand(self):
        if len(self.hand) >= 1:  #first card onli
            print(self.hand[0])
    
    def showHand(self):
        for card in self.hand:
            print(card)

    def resetHand(self):
        self.hand.clear()
    
    def totalHand(self):
        total = 0
        for card in self.hand:
            total += card.get_value()
            if card.rank == "A":
                if total > 21: # special condition ng ace
                    total -= 10
        return total

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


player = Player()
dealer = Dealer()

deck = Deck()

# menu
def gameLoop(playerIn, dealerIn):
    for _ in range(2):
        player.drawplayerCard(deck)
        dealer.drawCard(deck)

    while playerIn or dealerIn:
        print('\t'+'-'*74)
        print(f"\n\tDealer's cards \n\t{str(dealer.hand[0])} and X")
        print(f"\n\tYour cards \n\t{', '.join(map(str, player.hand))} \n\tTotal: {player.totalHand()}")
        

        if playerIn:
            print('\n\t1: Stay \n\t2: Draw ')
            while True:
                try:
                    stayOrDraw = int(input('\n\tChoice:'))
                    if stayOrDraw not in [1,2]:
                        raise ValueError
                    break
                except ValueError:
                    pass   
        if stayOrDraw == 1:
            playerIn = False
        else: 
            player.drawplayerCard(deck)
        if dealer.totalHand() > 16:
            dealerIn = False
        else:
            dealer.drawCard(deck)
        # terminate if one goes bust
        
        if player.totalHand() >= 21:
            break
        elif dealer.totalHand() >=21:
            break
    
def displayTable():
    #iayos format
    print(f"\n\tYou have {', '.join(map(str, player.hand))} for a total of {player.totalHand()} and the dealer has {', '.join(map(str, dealer.hand))} for a total of {dealer.totalHand()}")

def howToPlay():
    print('')
    pass
def viewDeck():
    clear()
    deck_sample = Deck()
    print('\t'+'-'*74)
    print('\n\t\t\t\t\t♦ ♣ ♥ ♠ \n')
    print('\t'+'-'*74)
    print('''\t\t    The game of Blackjack uses a standard 52-card deck. \n
        \tThe deck consists of four suits ♦ ♣ ♥ ♠ with 12 ranks each. \n 

        ''')
    deck_sample.printDeck()
    input('\n\t\t\t\tPress any key to go back...') 
    mainMenu()
    


def exitScreen():
    clear()
    print('\n\n\n\n\n\n\t'+'-'*74)
    print('\n\n\n\n\t\t\t   Thank you for playing Blackjack!')
    print('\n\t\t\t\t\t♦ ♣ ♥ ♠  ')
    print('\n\n\n\n\t'+'-'*74)
    pass

def gameOver():
    print('''\n\n\n
\t ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ██╗
\t██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗██║
\t██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝██║
\t██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚═╝
\t╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║██╗
\t ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝

\n\t\t\t1 Main Menu \t\t\t2 Exit
    ''')
    while True:
        try:
            back = int(input('\n\t\t\t\t\tEnter: '))
            if back == 1:
                mainMenu()
                break
            if back == 2:
                exitScreen()
                break
        except ValueError:
            pass
    
    

def startGame():
    clear()
    player.resetLife()
    playAgain = True
    print('\t'+'-'*74)
    print('\t\t\t\t\t♦ ♣ ♥ ♠  ')
    
    round=1
    deck = Deck()
    while playAgain:
        deck.shuffle()
        print('\t'+'-'*74)
        print(f'\tRound: {round}\n\tLives: {' '.join(map(str, player.lives))} ')
        gameLoop(playerIn, dealerIn)
        
        if player.totalHand() == 21:
            displayTable()
            print('\tBlackjack!')
        elif player.totalHand() == 21:
            displayTable()
            print('\tBlackjack! Dealer wins!')
            player.decreaseLife()
        elif player.totalHand() > 21:
            displayTable()
            print('\tBust! Dealer wins.')
            player.decreaseLife()
        elif dealer.totalHand() >21:
            displayTable()
            print('\tDealer bust! You win.')
            
        elif 21 - dealer.totalHand() < 21 - player.totalHand():
            displayTable()
            print('\tDealer wins!')
            player.decreaseLife()
        elif 21 - dealer.totalHand() > 21 - player.totalHand():
            displayTable()
            print('\tYou win!')

        deck.resetDeck()
        player.resetHand()
        dealer.resetHand()
        if not player.lives:
            playAgain = False
            gameOver()
            break
        round += 1
        while True:
            try:
                replay = int(input(f'\n\n\t\t\t\tContinue to the next round? \n\t\t\t\t\t  1: Yes \n\t\t\t\t\t  2: No \n\t\t\t\t\t  '))
                if replay == 2:
                    gameOver()
                    playAgain = False
                    break
                if replay == 1:
                    break
            except ValueError:
                pass

def mainMenu():
    clear()

    print('''
          
\t ██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗
\t ██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░░░░░██║██╔══██╗██╔══██╗██║░██╔╝
\t ██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░░░░░░██║███████║██║░░╚═╝█████═╝░
\t ██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╗░░██║██╔══██║██║░░██╗██╔═██╗░
\t ██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗
\t ╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
\n\t\t\t\t\t♦ ♣ ♥ ♠  ''')
    print('\t'+'-'*74)
    print('\n\t\t\t\t\tWelcome!')
    print('\n\t1 Start Game \n\t2 How to Play \n\t3 View Deck \n\t4 Exit\n')
    print('\t'+'-'*74)

    while True:
        try:
            menuChoice = int(input('\tEnter: '))
            if menuChoice == 1:
                startGame()
                break
            if menuChoice == 2:
                howToPlay()
                break
            if menuChoice == 3:
                viewDeck()
                break
            if menuChoice == 4:
                exitScreen()
                break
                
        except ValueError:
            pass


# mainMenu()


# ----------- TESTING -------------
# mainMenu()
# viewDeck()
startGame()
# gameOver()
pausee = input()
