import socket

class SendClientPacket():
    def sendPacket(message: str, host, port):
        #Create socket for client
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        #Send message to server
        sock.sendall(bytes(message.encode('utf-8')))

        #Print server response
        print(sock.recv(50))

        sock.close()
