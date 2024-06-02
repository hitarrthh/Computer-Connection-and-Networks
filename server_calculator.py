import socket
def calc(exp):
    try:
        return str( eval(exp))
    except:
        return 'error'
host = '127.0.0.1'
port = 1000
ss = socket.socket()
print("SOCKET CREATED")
ss.bind((host,port))
ss.listen()
print("WAITING FOR CONNECTION...")
conn,addr = ss.accept()
print("CONNECTION SUCCESSFUL WITH: ",addr)
x='1'
while True:
    x = conn.recv(1024).decode()
    ans = calc(x)
    z = ans.encode()
    conn.send(z)
conn.close()