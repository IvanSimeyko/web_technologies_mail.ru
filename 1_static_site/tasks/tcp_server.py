import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # making socket
s.bind(('0.0.0.0', 2222))   # making connetion whith this adress
s.listen(10)
while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)    # reading data
        if not data:
            break
        elif data == 'close':
            break
        conn.send(data)    # send data
    conn.close()
