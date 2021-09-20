import socket
#server_console

host = '127.0.0.1'  # local host (this pc)
port = 5000  # until 1024 not available

server = socket.socket()  # create server socket
server.bind((host, port))  # bind host address and port together (takes tuple as argument)
# configure how many client the server can listen simultaneously
# (i but the empty defalt value {backlog} it determine the queued items )
server.listen()
conn, address = server.accept()  # accept new connection( blocks and waits for an incoming connection)
print("Connection from: " + str(address))
while True: #endlees loop to accept data
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client
conn.close()  # close the connection

