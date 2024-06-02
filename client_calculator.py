import socket
host = '127.0.0.1'
port = 1000
cs = socket.socket()
cs.connect((host,port))
x = '1'
while True:
    x = input("enter expression: ")
    y = x.encode()
    cs.send(y)
    data = cs.recv(1024)
    z= data.decode()
    print("ANS: ",z)
cs.close()