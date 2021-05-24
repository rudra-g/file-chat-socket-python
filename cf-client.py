import socket

IP = "0.0.0.0"
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
def filerecive():
    print("[STARTING] Server is starting.")
    """ Starting a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Bind the IP and PORT to the server. """
    server.bind(ADDR)

    """ Server is listening, i.e., server is now waiting for the client to connected. """
    server.listen()
    print("[LISTENING] Server is listening.")

    while True:
        """ Server has accepted the connection from the client. """
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        """ Receiving the filename from the client. """
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename.")
        fl=input("save as: ")
        file = open(fl, "w")
        conn.send("Filename received.".encode(FORMAT))

        """ Receiving the file data from the client. """
        data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the file data.")
        file.write(data)
        conn.send("File data received".encode(FORMAT))

        """ Closing the file. """
        file.close()

        """ Closing the connection from the client. """
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")
        break

def filesend():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDR)
    fn=input("enter file name: ")
    """ Opening and reading the file data. """
    file = open(fn, "r")
    data = file.read()

    """ Sending the filename to the server. """
    client.send(fn.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """ Sending the file data to the server. """
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """ Closing the file. """
    file.close()

    """ Closing the connection from the server. """
    client.close()


def message():
     # client.py
    import time, socket, sys

    print("\nWelcome to Chat Room\n")
    print("Initialising....\n")
    time.sleep(1)

    s = socket.socket()
    shost = socket.gethostname()
    ip = socket.gethostbyname(shost)
    print(shost, "(", ip, ")\n")
    host = input(str("Enter server address: "))
    name = input(str("\nEnter your name: "))
    port = 1234
    print("\nTrying to connect to ", host, "(", port, ")\n")
    time.sleep(1)
    s.connect((host, port))
    print("Connected...\n")

    s.send(name.encode())
    s_name = s.recv(1024)
    s_name = s_name.decode()
    print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

    while True:
        message = s.recv(1024)
        message = message.decode()
        print("----------------------------")
        print(s_name, ":", message)
        print("----------------------------")
        message = input(str("Me : "))
        if message == "[e]":
            message = "Left chat room!"
            s.send(message.encode())
            print("\n")
            break
        s.send(message.encode())



if __name__ == "__main__":
    abc=1
    while(abc!=0):
        msg=input("1: chat room\n2: file send\n3: file recive\n4: quit\nenter your choice : ")
        if msg=="1":
            message()
        elif(msg=="2"):
            filesend()
        elif(msg=="3"):
            filerecive()
        elif(msg=="4"):
            abc=0
        else:
            print("\n please try again")