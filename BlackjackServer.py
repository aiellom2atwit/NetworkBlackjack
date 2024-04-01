import socket
from Player import Player
from Blackjack import Blackjack


class BlackjackServer():
    players = []
    startGame = False

    blackjackGame = None

    maxPlayers = 4

    def __init__(self):
        self.StartGame()


    def StartGame(self):
        #Create socket for server
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        port = 1234

        sock.bind(('', port))

        #Create Dealer/House
        self.players.append(Player(True, 0, socket.gethostname(), port))

        #Output to server console
        print("Listening for Players...")
        
        playerCount = 0
        #Loop to keep looking for client connections
        while True:
            sock.listen(30)
            cs, addr = sock.accept()

            print("Established connection with", addr)
            playerCount += 1
            print("Player Count:", playerCount, "/", self.maxPlayers)

            userResponse = cs.recv(1024).decode()
            if (userResponse == "Start"):
                playerCount += 1
                print(addr)
                self.CreatePlayerObj(playerCount, addr, 1234)

            cs.sendall(bytes('Accept'.encode('utf-8')))
            cs.close()


            userResponse = str(input("Start game? (Y/N): "))
            if userResponse.upper() == "Y":
                sock.close()
                self.blackjackGame = Blackjack(playerCount + 1, self.players)
                validResponse = True
                startGame = True
                break
                
    #Create a player object for joined players
    def CreatePlayerObj(self, playerIndex, ip, port):
        player = Player(False, playerIndex, ip, port)
        self.players.append(player)
            




