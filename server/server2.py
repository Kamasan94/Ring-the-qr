import socket

print("inizio")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.1.7",8000))
s.listen()

def start() :

    while True:
        # now our endpoint knows about the OTHER endpoint.
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established.")
        clientsocket.send(bytes("Hey there!!!","utf-8"))
        data = clientsocket.recv(1024).decode()
        print(data)
        
start()