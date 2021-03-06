import socket

# This can also be accomplished by using s = socket.socket() due to AF_INET and SOCK_STREAM being defaults
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ipaddr = '127.0.0.1'
port = 54321

#s.connect((ipaddr, port)) #not applicable to dgram sockets


# To send a string as a bytes-like object, add the prefix 'b' to the string. \n is used to go to the next line

s.sendto(b'Hello\n', (ipaddr, port))

# It is recommended that the buffersize used with revvfrom is a power of 2 and not a very large number of bits

response, conn = s.recvfrom(1024)

#In order to revieve a messag ethat is sent a a bytes like object, you must decode into utf-8 (default)

print(response.decode())

#s.close()i #not applicable for dgram sockets
