import socket
host = '127.0.0.1'
port = 1000
ss = socket.socket()
print("SOCKET SUCCESSFULLY CREATED")
ss.bind((host, port))  # Correct order of arguments
ss.listen()
print("WAITING FOR CONNECTION...")
conn, addr = ss.accept()  # Correct method name
print("CONNECTION SUCCESSFUL WITH", addr)
x = '1'
while x != 'bye':
    x = conn.recv(1024).decode()
    print("CLIENT: ",x)
    y = input("ENTER SERVER MESSAGE: ")
    data = y.encode()  # Correct method name
    conn.send(data)
conn.close()
