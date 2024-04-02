#Responsible for sending packets to the clients from server
import socket

class ServerResponse():

    def SendToAll(self, message, players, port, command):
        print(players)
        for player in players:
            #loop over every player
            currentIp = player.getIp()
            currentPort = player.getPort()

            if not player.isHouse():
                self.SendMessage(message, currentIp, currentPort, command)




    def SendMessage(self, message, ip, port, command):
        print(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print(ip)
        sock.connect((ip, 1235))

        sock.sendall(bytes(command.encode('utf-8')))
        print(command)

        ACK = str(sock.recv(50).decode())
        print(ACK)

        sock.close()

        if ACK == "ACK":
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sock.connect((ip, 1235))
            print("Sending message")

            sock.sendall(bytes(message.encode('utf-8')))

            response = str(sock.recv(50).decode())

            sock.close()

            return response
        else:
            sock.close()
            print("NACK")





