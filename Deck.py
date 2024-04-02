import random
from Card import Card
from Card import Suit
from Card import Value


class Deck():
    cards = []
    
    cardsLeft = 0

    #Constructor
    def __init__(self):
        #Generate new shuffled deck when initialized
        self.GenerateDeck()
    

    #Generates a new deck
    def GenerateDeck(self):
        #Generate a full deck of every suit + value
        for suit in list(Suit):
            for val in list(Value):
                self.cards.append(Card(suit, val))
                self.cardsLeft += 1
        #Shuffle cards
        self.cards = self.Shuffle(self.cards)




    #Takes array of cards and shuffles it randomly
    def Shuffle(self, cards):
        return random.sample(cards, len(cards))


    def IsEmpty(self):
        return (self.cardsLeft == 0)

    def DrawCard(self):
        #If deck is empty create new shuffled deck
        if self.IsEmpty():
            self.GenerateDeck()

        #Return the last card from cards
        self.cardsLeft -= 1
        return self.cards.pop()