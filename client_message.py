import socket
host = '127.0.0.1'
port = 1000
cs = socket.socket()
cs.connect((host, port))  # Connect to the server
x = '1'
while x != 'bye':
    x = input("ENTER CLIENT MESSAGE: ")
    y = x.encode()
    cs.send(y)
    data = cs.recv(1024)
    z = data.decode()
    print("SERVER:", z)
cs.close()
