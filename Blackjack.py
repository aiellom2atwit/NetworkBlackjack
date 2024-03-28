#import the library for network-related functionalities
import socket

from Deck import Deck
from Card import Card
from Player import Player
from Card import Suit
from Card import Value
from ServerResponse import ServerResponse




class Blackjack():
    deck = []
    players = []

    def __init__(self, playerCount, players):
        self.deck = Deck()
        self.players = players

        self.StartGame()

    
    def CheckBust(self, player):
        return (player.GetTotalValue() > 21)

    def StartGame(self):
        for player in self.players:
            self.HitCard(player)
        

 

    def HitCard(self, player: Player):
        playerIndex = player.playerIndex
        card = self.deck.DrawCard()

        player.AddCard(card)

        output = card.readContents()

        ServerResponse.SendResponse(ServerResponse, output, player.getIp(), player.getPort(), "NONE")