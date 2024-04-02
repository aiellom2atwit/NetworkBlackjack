from Card import Card
from Deck import Deck

class Hand():
    cardTotal = 0
    cardLen = 0
    cards = []

    def AddCard(self, card):
        self.cards.append(card)
        self.cardTotal += card.getValue()
        self.cardLen += 1

    def __str__(self):
        output = "---------------------"
        for card in self.cards:
            output += "\n"
            output += str(card)
        output += "\nTotal Cards: "
        output += str(self.cardTotal)
        output += "\n(21 is Bust.)"

        return output

    def totalValue(self):
        return self.cardTotal

    def length(self):
        return self.cardLen