# Responsible for sending packets to the clients from server
import socket


class ServerResponse():

    # def __init__(self):
    #     print("int server")

    def SendToAll(self, message, players, port, command):
        print(players)
        for player in players:
            # loop over every player
            currentIp = player.getIp()
            currentPort = player.getPort()

            if not player.isHouse():
                self.SendMessage(message, currentIp, currentPort, command)

    def SendMessage(self, message, ip, port, command):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        # print(ip)


        # ip here is a tuple with the actual ip and port
        sock.connect((str(ip[0]), 1235))

        sock.sendall(bytes(command.encode('utf-8')))




        ACK = str(sock.recv(50).decode())
        print(str(command))

        # ACK = "ACK"
        print(ACK)

        sock.close()

        match str(ACK):
            case "ACK":
                sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)

                sock.connect((ip, 1235))
                print("Sending message")

                sock.sendall(bytes(command.encode('utf-8')))

                response = str(sock.recv(50).decode())

                sock.close()

                return response
            case _:
                sock.close()
                print("NACK")
