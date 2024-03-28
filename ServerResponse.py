#Responsible for sending packets to the clients from server
import socket

class ServerResponse():
    clientPort = 1235

    def SendResponse(self, message, ip, port, command):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((ip, self.clientPort))

        sock.sendall(bytes(command.encode('utf-8')))

        ACK = str(sock.recv(50).decode())
        print(str(command))
        print(ACK)

        sock.close()

        match str(ACK):
            case "ACK":
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                sock.connect((ip, self.clientPort))

                sock.sendall(bytes(command.encode('utf-8')))

                response = str(sock.recv(50).decode())

                sock.close()
            case _:
                sock.close()
                print("NACK")





