# client.py

import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Totmatic2
#soc.connect(("192.168.9.198", 5045))

#Discriminador de tags
soc.connect(("192.168.9.198", 8051))

while (1):
    result_bytes = soc.recv(4096) # the number means how the response can be in bytes
    result_string = result_bytes.decode("utf8") # the return will be in bytes, so decode

    print("Result from server is {}".format(result_string))


soc.close()