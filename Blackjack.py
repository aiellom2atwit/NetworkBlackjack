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
        self.sr = ServerResponse()
        self.StartGame()

    
    def CheckBust(self, player):
        return (player.getTotal() > 21)

    def StartGame(self):
        #Draw initial cards
        initialCards = 2
        self.players = self.generateStartingHand(self.players, initialCards)
        #send cards to clients
        
        print(self.players)
        #turn LOOP1
        for player in self.players:
            if player.isHouse():
                self.HouseTurn(player)
                #House turn
            else:
                print("Player Turn")
                #not house
                self.PlayerTurn(player)
        
        print("HOUSE'S TURN")
        housePlayer = self.players[0]
        houseValue = self.HouseTurn(housePlayer)

        # check for winners
        winnerMsg = self.CheckWinner(self.players)
        print(winnerMsg)

        # send winners to client
        ServerResponse.SendToAll(winnerMsg, self.players, "END", 0)
        

    def HitOrStand(self, player):
        hand_output = str(player.getHand())

        print(hand_output)

        messageFlag = ServerResponse.SendMessage(hand_output, player.getIp(), player.getPort(), "HITORSTAND")

        if messageFlag == "True":
            generalMessage = hand_output + "HIT"
            ServerResponse.SendMessage(generalMessage, player.getIp(), player.getPort(), player.playerIndex)
            return True

        generalMessage = hand_output + "STAND"
        print(generalMessage)

        ServerResponse.SendMessage(generalMessage, player.getIp(), player.getPort(), player.playerIndex)

        return False


    def PlayerTurn(self, player):
        #Hit sequential cards until player requests to stop
        turnOver = not self.HitOrStand(player)
        playerIndex = player.playerIndex
        returnMsg = ""

        while not turnOver:
            card = self.deck.DrawCard()
            returnMsg += card.toString()

            player.AddCard(card)

            returnMsg = card.readContents()
            print(returnMsg)

            ServerResponse.SendMessage(returnMsg, player.getIp(), player.getPort(), "NONE")

            turnOver = not self.HitOrStand(player)


    def HouseTurn(self, player):
        returnMsg = ""
        #Method to determine what the house does on a turn
        #If House starts with 21, reset
        if (player.getTotal() == 21 and player.getHand().length() == 2):
            returnMsg += "RESET"
            player.resetHand()
            player = self.generateStartingHand(player, 2)
            return self.HouseTurn(player)
        #17 and above = stand
        if (player.getTotal() >= 17):
            #21 = House wins
            if (player.getTotal() == 21):
                returnMsg += str(player.getTotal())
            #>21 House busts
            if (player.getTotal() >= 21):
                returnMsg += str(player.getTotal())
            print(returnMsg)

            ServerResponse.SendToAll(returnMsg, self.players, "NONE", 0)
            return player.getTotal()
        
        #16 and below = hit
        if (player.getTotal() <= 16):
            drawnCard = self.deck.DrawCard()
            player.AddCard(drawnCard)
            return self.HouseTurn(player)
          

    def generateStartingHand(self, players, cardAmount):
        for i in range(0, cardAmount):
            for player in players:
                drawnCard = self.deck.DrawCard()
                player.AddCard(drawnCard)
        print("Inital Player Cards:\n")
        for player in players:
            if not player.isHouse():
                ServerResponse.SendMessage(str(player), player.getIp(), player.getPort(), "NONE")
        return players

    def CheckWinner(self, players):
        # TODO
        scores = {}
        houseScore = int
        returnMsg = ""
        returnMsg += "GAME RESULT"
        for player in players:
            if player.isHouse():
                houseScore = player.getTotal()
                index = player.getIndex()
                scores[index] = houseScore
                #isHouse
            else:
                score = player.getTotal()
                index = player.getIndex()
                scores[index] = score
                
                #if player score >= house, player wins
                if score >= houseScore:
                    ServerResponse.SendMessage(
                            f" Win -> you with value: {score}, House lost with value {houseScore}\n", player.getIp(),
                            player.getPort(), "NONE")
                #if player score < house, house wins
                elif score < houseScore:
                    ServerResponse.SendMessage(
                            f"Lost -> you with value: {score}, House won with value {houseScore}\n", player.getIp(),
                            player.getPort(), "NONE")
        returnMsg += "Winner is player "
        for index, score in scores.items():
            returnMsg += f"\n{index} with a score of {score}"
        return returnMsg