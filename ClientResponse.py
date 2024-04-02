import socket


class ClientResponse():
    #Handles hit and stand functionality for client along with ack
    port: int

    """
     def __init__ to listen to the server , then send the message back to server  
    
    
    """





    def __init__(self, port):
        self.port = port
        self.SendMessage(self.port)

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
        




    def SendMessage(self, port):
        print("Sending Message from client...")
        NeedsYesOrNo = False
        NeedsHitOrStand = False
        NeedsNone = False
        NeedsWinner = False

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.bind(('', port))

        #Create loop to keep client checking for input
        GameEnd = False
        while not GameEnd:
            sock.listen(1000)

            cs, addr = sock.accept()

            #Get message from server
            serverResponse = str(cs.recv(1000).decode())
            

            if NeedsWinner:
                print(serverResponse)
                NeedsWinner = False
                EndGame = True
                cs.sendall(bytes('ACK'.encode('utf-8')))
                cs.close()
                sock.close()
                break

            if NeedsYesOrNo:
                print(serverResponse)
                print("Your Turn: ")
                NeedsYesOrNo = False
                cs.sendall(self.YesOrNo(serverResponse).encode('utf-8'))
                cs.close()
                break

            if NeedsHitOrStand:
                print(serverResponse)
                print("Your Turn: ")
                NeedsHitOrStand = False
                cs.sendall(bytes(self.HitOrStand(0, serverResponse).encode('utf-8')))
                cs.close()
                break
            
            if NeedsNone:
                print(serverResponse)
                NeedsNone = False
                print("Ping message")
                
                cs.sendall(bytes('ACK'.encode('utf-8')))
                cs.close()
                
            
            #Set booleans based on message
            match serverResponse:
                case "YESORNO":
                    NeedsYesOrNo = True
                    cs.sendall(self.YesOrNo(0, serverResponse).encode('utf-8'))
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
                    GameEnd = True
                    cs.sendall(bytes('ACK'.encode('utf-8')))
                    cs.close()
                    sock.close()
