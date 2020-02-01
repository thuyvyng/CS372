# from socket import *
# import sys
#
# HOST = "localhost"
# PORT = int(sys.argv[1])
#
# s = socket(AF_INET,SOCK_STREAM) #what does this mean
# s.bind((HOST, PORT))
# s.listen(1)
# print("Server is listening....")
#
# conn, addr = s.accept()
# print("Connected with" +addr[0]+":"+str(addr[1]))
#
# data = conn.recv(1024)
#
# print("Sending file", data.decode()+"...")
#
# f = open(data,"rb")
# packet = f.read(1024)
#
# while packet:
#     conn.send(packet)
#     packet = f.read(1024)
#
# s.close()

from socket import *
import sys

HOST = "localhost"
PORT = int(sys.argv[1])

s = socket(AF_INET,SOCK_STREAM) #what does this mean
s.bind((HOST, PORT))
s.listen(1)
print("Server is listening....")


while True:
    conn, addr = s.accept()
    print("Connected from ",addr)

    data = conn.recv(1024)

    print("Sending file", data.decode()+"...")

    f = open(data,"rb")
    packet = f.read(1024)

    while packet:
        conn.send(packet)
        packet = f.read(1024)

    f.close()

    print("Done!")
    conn.close()
    sys.exit(0)
