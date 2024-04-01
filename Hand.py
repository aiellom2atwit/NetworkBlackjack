from Card import Card
from Deck import Deck

class Hand():
    cardTotal = 0
    cards = []

    def AddCard(self, card):
        self.cards.append(card)
        self.cardTotal += card.getValue()

    def PlayCard():
        pass

    def PrintHand(self):
        output = "---------------------"
        for card in self.cards:
            output += "\n"
            output += card.toString()
        output += "\nTotal Cards: "
        output += str(self.cardTotal)
        output += "\n(21 is Bust.)"

        return output

    def getTotalCardValue(self):
        return self.cardTotal