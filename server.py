import socket
import sys
import time
print("Chatter")
print("by Daniel Hsieh")
ns = socket.socket()
hostname = socket.gethostname()
sip = socket.gethostbyname(hostname)
port = 8080
ns.bind((hostname, port))
print("This is your IP: ", sip)
name = input('Enter name:')
ns.listen()
conn, addr= ns.accept()
print("Hey, we finally recieved a connection!")
client = (conn.recv(1024)).decode()
print(client + ' has connected.')
conn.send(name.encode())
while True:
    message = input('You : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)