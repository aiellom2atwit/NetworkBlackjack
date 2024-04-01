import socket


class ClientResponse():
    #Handles hit and stand functionality for client along with ack
    port = int

    def YesOrNo(self, message):
        print(message)

        validInput = False
        while (validInput == False):
            userResponse = str(input("(Y/N): "))
            match (userResponse.upper()):
                case "Y":
                    validInput = True
                    return 'True'
                case "N":
                    validInput = True
                    return 'False'
                case _:
                    print("Invalid input: \"{userResponse}\"\nEnter (Y/N).")

    def HitOrStand(self, message):
        print(message)

        validInput = False
        while (validInput == False):
            userResponse = str(input("Hit or Stand (H/S): "))
            match (userResponse.upper()):
                case "H":
                    validInput = True
                    return 'True'
                case "S":
                    validInput = True
                    return 'False'
                case _:
                    print("Invalid input: \"{userResponse}\"\nEnter (H/S).")
        


    def __init__(self, port):
        self.port = port
        self.SendResponse(self.port)

    def SendResponse(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.bind(('', port))

        #Create loop to keep client checking for input
        GameOver = False
        while (GameOver == False):
            sock.listen(1000)

            cs, addr = sock.accept()

            NeedsYesOrNo = False
            NeedsHitOrStand = False
            NeedsNone = False
            NeedsWinner = False

            EndGame = False
            while not EndGame:
                #Get message from server
                serverResponse = str(cs.recv(1000).decode())

                #Set booleans based on message
                match serverResponse:
                    case "YESORNO":
                        NeedsYesOrNo = True
                        cs.sendall(self.YESORNO(0, serverResponse).encode('utf-8'))
                        cs.close()
                    case "HITORSTAND":
                        NeedsYesOrNo = True
                        cs.sendall(bytes(self.HitOrStand(serverResponse).encode('utf-8')))
                        cs.close()
                    case "NONE":
                        NeedsNone = True
                        cs.sendall(bytes('ACK'.encode('utf-8')))
                        cs.close()
                    case "END":
                        NeedsWinner = True
                        cs.sendall(bytes('ACK'.encode('utf-8')))
                        cs.close()


                if (NeedsWinner):
                    NeedsWinner = False
                    EndGame = True
                    print(serverResponse)
                    cs.sendall(bytes('ACK'.encode('utf-8')))
                    cs.close()
                    sock.close()

                if (NeedsYesOrNo):
                    print("Your Turn: ")
                    NeedsYesOrNo = False
                    cs.sendall(self.YesOrNo(serverResponse).encode('utf-8'))
                    cs.close()

                if (NeedsHitOrStand):
                    print("Your Turn: ")
                    NeedsHitOrStand = False
                    cs.sendall(bytes(self.HitOrStand(0, serverResponse).encode('utf-8')))
                    cs.close()
            
                if (NeedsNone):
                    print(serverResponse)
                    print("Ping message")
                    cs.sendall(bytes('ACK'.encode('utf-8')))
                    cs.close()