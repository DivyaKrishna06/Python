import socket

s = socket.socket()
print ("Socket successfully created")

port = 40674 #Reserve port

s.bind(('', port))
print ("socket binded to %s" %(port))

s.listen(5)
print ("socket is listening")

while True:

	# Establish connection with client.
	c, addr = s.accept()
	print ('Got connection from', addr )

	c.send(b'Thank you for connecting')

	c.close() # Client connection close