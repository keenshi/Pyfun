import random
from xml.sax.handler import feature_external_ges

suits = ["Hearts","Clubs","Diamonds","Spades"]
ranks=['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

class Card:
    def __init__(self,suits,rank): 
        self.suits = suits
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suits}'


class Deck:
    def __init__(self):
        self.alldeck=[]
        for suit in suits:
            for rank in ranks:
                self.alldeck.append(Card(suit,rank))
        
    def shuffle(self):
        random.shuffle(self.alldeck)
    
    def deal_one(self):
        return self.alldeck.pop()
    
        
class Player:
    def __init__(self,name):
        self.name = name
        self.allcards=[]
    
    def remove_one(self):
        return self.allcards.pop(0)

    def add_cards(self,newcards):
        if type(newcards) == type([]):
            self.allcards.extend(newcards) 
        else:
            self.allcards.append(newcards) 

    def __str__(self):
        return f'{self.name} has {len(self.allcards)} cards.'

Player1=Player('P1')
Player2=Player('P2')
newdeck=Deck()
newdeck.shuffle()
for x in range(26):
    Player1.add_cards(newdeck.deal_one())
    Player2.add_cards(newdeck.deal_one())

game_on=True
roundno=0
while game_on:
    roundno+=1
    print(f'Round {roundno}.')

    if len(Player1.allcards)==0:
        print(f'{Player1.name} has no cards left. {Player2.name} has won.') #working
        game_on = False
        break

    elif len(Player2.allcards)==0:
        print(f'{Player2.name} has no cards left. {Player1.name} has won.')
        game_on = False
        break

    else:
        pass

    Player1_tablecards=[]
    Player1_tablecards.append(Player1.remove_one())

    Player2_tablecards=[]
    Player2_tablecards.append(Player2.remove_one())

    at_war=True
    while at_war:
        if Player1_tablecards[-1].value > Player2_tablecards[-1].value:
            Player1.add_cards(Player1_tablecards)
            Player1.add_cards(Player2_tablecards)
            at_war=False

        elif Player1_tablecards[-1].value < Player2_tablecards[-1].value:
            Player2.add_cards(Player1_tablecards)
            Player2.add_cards(Player2_tablecards)
            at_war=False

        else:
            print('WAR')
            if len(Player1.allcards) < 5:
                print(f'{Player1.name} does not have enough cards for a war. {Player2.name} wins') #working
                game_on=False
                break

            elif len(Player2.allcards) < 5:
                print(f'{Player2.name} does not have enough cards for a war. {Player1.name} wins') #working
                game_on=False
                break
            for num in range(5):
                Player1_tablecards.append(Player1.remove_one())
                Player2_tablecards.append(Player2.remove_one())



