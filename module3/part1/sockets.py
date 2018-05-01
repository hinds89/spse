#!/usr/bin/env python

import socket
port = 8000

# create TCP socket which will listen on specific port on server
# address family for internet based applications will typically use
# AF_INET. The second argument is the kind of scoket (from reliability
# perspective, since we use TCP we will use SOCK_STREAM, UDP is different)
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# bind socket to port and interface
# multihomed - means multiple network interfaces
tcpSocket.bind(("0.0.0.0", port))

# start listening
# the argument is the number of concurrent clients the socket can handle
tcpSocket.listen(2)

print "See if you can connect to the server by running netcat:"
print "nc %s %d"%("0.0.0.0", 8000)

print "Waiting for a Client ..."
# A client socket is created for each client.  The IP and port is of the client
# accept is a blocking call (it waits and doesn't return until a client 
# connects).
(client, (ip, port)) = tcpSocket.accept()

# once a client is connected you can use client.send("<string>") to send a string
client.send("Welcome to the SPSE Course")

# You can also receive, the argument is the size of the buffer
data = client.recv(2048)

# code for an echo server
print "Received connection from : ", ip
print "Starting Echo output .... "

data = 'dummy'

while len(data) :
	data = client.recv(2048)
	print "Client sent: ", data
	client.send("Client sent: " + data)


print "Closing connection ..."
client.close()

print "Shutting down server ..."
tcpSocket.close()
