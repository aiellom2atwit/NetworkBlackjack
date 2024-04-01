
import ClientResponse
from SendClientPacket import SendClientPacket

ip = str

#Have user specify IP if not localhost
responseOk = False
while (responseOk == False):
    userResponse = str(input("Would you like to connect to localhost? (Y/N): "))
    match userResponse.upper():
        case "Y":
            ip = "localhost"
            responseOk = True
        case "N":
            ip = str(input("Enter server IP: "))
            responseOk = True
        case _:
            print("Invalid Input: \"", userResponse, "\"\nPlease enter only (Y/N).")

port = 1234

#Ask the Client if they would like to connect to the server
responseOk = False
while (responseOk == False):
    userResponse = str(input("Connect (Y/N): "))
    match userResponse.upper():
        case "Y":
            SendClientPacket.sendPacket("Start", ip, 1234)
    
            ClientResponse.ClientResponse(1235)
            responseOk = True
            break
        case "N":
            print("Connection terminated")
            responseOk = True
            break
        case _:
            print("Invalid Input: ", userResponse.upper, "Please enter only (Y/N).")
    