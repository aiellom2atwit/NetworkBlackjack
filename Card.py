
from enum import Enum


class Suit(Enum):
    HEARTS = 0
    CLUBS = 1
    DIAMONDS = 2
    SPADES = 3

class Value(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    JACK = 10
    QUEEN = 10
    KING = 10
    ACE = 11


class Card():
    suit = Suit
    value = Value

    #Constructor for card class
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    #Returns integer value 
    def getValue(self):
        return self.value.value

    def getStringValue(self):
        return str(Value(self.value).name)

    def getStringSuit(self):
        return str(Suit(self.suit).name)

    def __str__(self):
        return str(self.getStringValue() + " of " + self.getStringSuit())



