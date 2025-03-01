'''TCP_Client'''

import socket

HOST = "www.google.com"
PORT = 80

# create a socket object

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client

client.connect((HOST, PORT))

# send some data

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive some data

response = client.recv(4096)

print(response.decode())
client.close()
