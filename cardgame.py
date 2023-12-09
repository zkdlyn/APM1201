import random
playerIn = True
dealerIn = True

bet = None
# cards 

suits = ["\u2663", "\u2665", "\u2666", "\u2660"] # club heart diamond spade
ranks = [2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'A']

deck = []

playerHand = []
dealerHand = []

total = 0 
# card values 
# gawin tong function idk
card_values = {}
for suit in suits:
    for rank in ranks:
        card = f'{rank}{suit}'
        faces = ['J', 'Q', 'K']
        deck.append(card)
        if isinstance(rank, int):
            card_values[card] = rank
        elif rank in faces:
            card_values[card] = 10
        else:
            if total > 11:
                card_values[card] = 1
            else: 
                card_values[card] = 11


# deal cards
def dealCard(turn):
    random.shuffle(deck)
    card = deck.pop()
    turn.append(card)
    
# calculate total per hand

def cardTotal(turn, total):
    total = 0
    # ace has val of 11, if adding it will total greater than 21, it instead has value of 1
    for card in turn:
        total += card_values[card]
    return total

# check winner
def showDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand)>2:
        return dealerHand[0], dealerHand[1]

# game loop
def startGame(playerIn, dealerIn):  
    for _ in range(2):
        dealCard(dealerHand)
        dealCard(playerHand)

    while playerIn or dealerIn:
        print(f"Dealer's cards \n{showDealerHand()} and X")
        print(f"\nYour cards \n{', '.join(map(str, playerHand))} \nTotal: {cardTotal(playerHand, total)}")
        if playerIn:
            stayOrDraw = input('\n1: Stay \n2: Draw \n')
        if cardTotal(dealerHand, total)>16:
            dealerIn = False
        else:
            dealCard(dealerHand)
        if stayOrDraw == '1':
            playerIn = False
        # terminate if one goes bust
        else: 
            dealCard(playerHand)
        if cardTotal(playerHand, total) >= 21:
            break
        elif cardTotal(dealerHand, total) >=21:
            break





playAgain = True 

print('Hi! Welcome to Blackjack')
print('For how much do you want to play?')
bet = int(input('Enter: '))

playerBet = dealerBet = bet
print('\n\n')
print(f'Your money: {playerBet}')
while playAgain:
    print('How much are you betting this round?')
    roundBet = int(input('Enter: '))
    print('\n')
    startGame(playerIn, dealerIn)
    
    
    if cardTotal(playerHand, total) == 21:
        print(f"\nYou have {', '.join(map(str, playerHand))} for a total of {cardTotal(playerHand, total)} and the dealer has {', '.join(map(str, dealerHand))} for a total of {cardTotal(dealerHand,total)}")
        print('Blackjack!')
        playerBet += roundBet
    elif cardTotal(dealerHand, total) == 21:
        print(f"\nYou have {', '.join(map(str, playerHand))} for a total of {cardTotal(playerHand, total)} and the dealer has {', '.join(map(str, dealerHand))} for a total of {cardTotal(dealerHand,total)}")
        print('Blackjack! Dealer wins!')
    elif cardTotal(playerHand, total)>21:
        print(f"\nYou have {', '.join(map(str, playerHand))} for a total of {cardTotal(playerHand, total)} and the dealer has {', '.join(map(str, dealerHand))} for a total of {cardTotal(dealerHand,total)}")
        print('Bust! Dealer wins.')
    elif cardTotal(dealerHand, total)>21:
        print(f"\nYou have {', '.join(map(str, playerHand))} for a total of {cardTotal(playerHand, total)} and the dealer has {', '.join(map(str, dealerHand))} for a total of {cardTotal(dealerHand,total)}")
        print('Bust! You win.')
    elif 21 - cardTotal(dealerHand,total)< 21 - cardTotal(playerHand, total):
        print(f"\nYou have {', '.join(map(str, playerHand))} for a total of {cardTotal(playerHand, total)} and the dealer has {', '.join(map(str, dealerHand))} for a total of {cardTotal(dealerHand,total)}")
        print('Dealer wins!')
    elif 21 - cardTotal(dealerHand,total) > 21 - cardTotal(playerHand, total):
        print(f"\nYou have {', '.join(map(str, playerHand))} for a total of {cardTotal(playerHand, total)} and the dealer has {', '.join(map(str, dealerHand))} for a total of {cardTotal(dealerHand,total)}")
        print('You win!')

    if playerBet == 0:
        print('Game end! You have no more money left. Try your luck again next time.')
        playAgain = False
    replay = input(f'\n\nDo you want to play another round? \n1: Yes \n2: No \n')
    if replay == '2':
        print('Game end! Thank you for playing Blackjack!')
        playAgain = False
end = input()