import random
playing=True

suits=['Hearts','Spades','Clubs','Diamonds']
ranks=['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}


class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}.'

class Deck:
    def __init__(self):
        self.Deckcards=[]
        
        for suit in suits:
            for rank in ranks:
                self.Deckcards.append(Card(suit,rank))
    
    def shuffle(self):
        random.shuffle(self.Deckcards)

    def __str__(self):
        Cardname=''
        for cards in self.Deckcards:
            Cardname += '\n' + cards.__str__()
        return f'The Deck has ' + Cardname

    def deal(self):
        single_card=self.Deckcards.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0

    def add_cards(self,card):
        self.cards.append(card)
        self.value += values[card.rank] 

        if card.rank=='Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.aces -= 1
            self.value -= 10

class chips:
    def __init__(self):
        self.total=100
        self.bet=0

    def winbet(self):
        self.total += self.bet

    def losebet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet=int(input('Please desired amount to bet.'))
        except:
            print('Please enter an interger type, not a string.')
        else:
            if chips.bet > chips.total:
                print(f'Sorry! You do not have enough chips. {chips.total} in inventory')
            else:
                break

def hit(Deck,Hand):
    Hand.add_cards(Deck.deal())
    Hand.adjust_for_ace()

def hit_or_stand(deck,Hand):
    global playing

    while True:
        x = input('Hit or Stand. (H or S)')
        if(x).upper()=='H':
            print('Hit!')
            hit(deck,Hand)
        elif(x).upper()=='S':
            print('Player stands!')
            playing=False
        else:
            print('Sorry, Please enter again.')
            continue
        break

def show_some(player,dealer):
    print("Dealer's cards: \n Hidden card!")
    print(dealer.cards[1])

    print("Player's cards:")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    print("Dealer's cards:")
    for card in dealer.cards:
        print(card)
    print(f"The Dealer's hand is {dealer.value}")

    print("Player's cards:")
    for card in player.cards:
        print(card)
    print(f"The Player's hand is {player.value}")

def player_busts(player,dealer,chips):
    print('Player busted!')
    chips.losebet()

def player_wins(player,dealer,chips):
    print('Player wins!')
    chips.winbet()

def dealer_busts(player,dealer,chips):
    print('Dealer busted!')
    chips.winbet()

def dealer_wins(player,dealer,chips):
    print('Dealer wins!')
    chips.losebet()

def push(player,dealer):
    print('Dealer and Player tie! PUSH!')



while True:
    
    print('Welcome to BlackJack')
    deck = Deck()
    deck.shuffle()
    
    player = Hand()
    player.add_cards(deck.deal())
    player.add_cards(deck.deal())
    
    dealer = Hand()
    dealer.add_cards(deck.deal())
    dealer.add_cards(deck.deal())
    
    player_chips=chips()

    take_bet(player_chips)

    show_some(player,dealer)

    while playing:
        hit_or_stand(deck,player)

        show_some(player,dealer)

        if player.value > 21:
            player_busts(player,dealer,player_chips)
            break
    
    if player.value <= 21:
        while dealer.value<17:
            hit(deck,dealer)
        show_all(player,dealer)
        if dealer.value > 21:
            dealer_busts(player,dealer,player_chips)

        elif dealer.value > player.value:
            dealer_wins(player,dealer,player_chips)

        elif dealer.value < player.value:
            player_wins(player,dealer,player_chips)

        else:
            push(player,dealer)        
    
    print("\nPlayer's winnings stand at",player_chips.total)
    
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break



        
        
    