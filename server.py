import socket
import linda
# import thread module
from _thread import *
import threading

print_lock = threading.Lock()

space = linda.Linda()

# thread fuction
def threaded(c):
    while True:

        # data received from client
        data = c.recv(1024).decode()
        data = data.split()

        if (data[0] == "rd"):
            messageout = space._rd(data[1])
        elif (data[0] == "in"):
            s = ' '
            messageout = space._in(data[1], data[2], s.join(data[3:data.__len__()]))
        elif (data[0] == "out"):
            s = ' '
            messageout = space._out(data[1], data[2], s.join(data[3:data.__len__()]))

        # send back reversed string to client
        c.send(messageout.encode())
        # connection closed
    c.close()

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(5)  # accept new connection
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))

        start_new_thread(threaded, (conn,))

        # linda operations

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()