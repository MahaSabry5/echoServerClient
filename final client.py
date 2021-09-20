import socket
#client_console

host = '127.0.0.1'  # as both code is running on same pc
port = 5000  # socket server port number until 1024 not available

client = socket.socket()  # create client socket
client.connect((host, port))  # connect to the server
message = input(" -> ")  # take input

while message.lower().strip() != 'bye': #to terminate program
        client.send(message.encode())  # send message (seq of bytes)
        data = client.recv(1024).decode()  # receive response from server

        print('Received from server: ' + data)  # show in terminal
        message = input(" -> ")  # again take input
client.close()  # close the connection

