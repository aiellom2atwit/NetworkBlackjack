from Hand import Hand
from Card import Card
from Card import Value
from ServerResponse import ServerResponse

class Player():
    playerIndex = 0
    isTurn = False

    hand = None

    ip: str
    port: int

    isHouse = False

    valueTotal = 0

    def __init__(self, isHouse, playerIndex, ip, port):
        self.playerIndex = playerIndex
        self.hand = Hand()
        self.isTurn = False
        self.ip = ip
        self.port = port
        self.isHosue = isHouse

    def AddCard(self, card):
        self.hand.AddCard(card)
        self.valueTotal += card.getValue()


        sr = ServerResponse()

        #print(self.hand)
        sr.SendMessage(self.hand.PrintHand(), self.ip, self.port, "NONE")

    def getHand(self):
        return self.hand

    def GetValueTotal(self):
        return self.valueTotal
    
    def getIp(self):
        return self.ip

    def isHouse(self):
        return self.isHouse;

    def getPort(self):
        return self.port

    def resetHand(self):
        self.hand = Hand()

    def getIndex(self):
        return self.playerIndex
