import socket


class ClientResponse():
    #Handles hit and stand functionality for client along with ack
    port = 1235

    """
     def __init__ to listen to the server , then send the message back to server  
    
    
    """





    def __init__(self):
        #self.port = port
        self.ClientLoop(self.port)


    def ClientLoop(self, port):
        NeedsYesOrNo = False
        NeedsHitOrStand = False
        NeedsNone = False
        NeedsWinner = False

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.bind(('', port))

        GameEnd = False
        while not GameEnd:
            print("Waiting for message from server...")

            sock.listen(1000)

            cs, addr = sock.accept()

            #Get message from server
            serverResponse = str(cs.recv(1000).decode())
            print("Recieved message from server.")

            if NeedsWinner:
                print(serverResponse)
                NeedsWinner = False
                GameEnd = True
                self.SendMessage('ACK', cs)
                cs.close()
                sock.close()
                break

            if NeedsYesOrNo:
                print("Your Turn: ")
                NeedsYesOrNo = False
                sendMessage = self.YesOrNo(serverResponse)
                self.SendMessage(sendMessage, cs)
                cs.close()
                break

            if NeedsHitOrStand:
                print("Your Turn: ")
                NeedsHitOrStand = False
                sendMessage = self.HitOrStand(serverResponse)
                self.SendMessage(sendMessage, cs)
                cs.close()
                break
            
            if NeedsNone:
                print(serverResponse)
                NeedsNone = False
                print("Ping message")
                
                self.SendMessage('ACK', cs)
                cs.close()
            
            #Set booleans based on message
            match serverResponse:
                case "YESORNO":
                    NeedsYesOrNo = True
                    sendMessage = self.YesOrNo(serverResponse)
                    self.SendMessage(sendMessage, cs)
                    cs.close()
                case "HITORSTAND":
                    NeedsYesOrNo = True
                    sendMessage = self.HitOrStand(serverResponse)
                    self.SendMessage(sendMessage, cs)
                    cs.close()
                case "NONE":
                    NeedsNone = True
                    self.SendMessage('ACK', cs)
                    cs.close()
                case "END":
                    NeedsWinner = True
                    GameEnd = True
                    self.SendMessage('ACK', cs)
                    cs.close()
                    sock.close()
            


    def YesOrNo(self, message):
        print(message)
        print("YeOrNO")
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

        print("HitOrStand")
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
        



    def SendMessage(self, message : str, cs):
        encodedMessage = message.encode('utf-8')
        
        cs.sendall(bytes(encodedMessage))

            
                
            
            
