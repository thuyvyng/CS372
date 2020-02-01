from socket import *
import sys

HOST = "localhost"
PORT = int(sys.argv[1])

s = socket(AF_INET,SOCK_STREAM)
s.connect((HOST, PORT))

file_name = input('Insert file name')
print(file_name)
s.send(file_name.encode())

f = open(file_name,"wb") #victor says its wb?

while True:
    data = s.recv(1024)
    if not data:
        break
    f.write(data)

# message = s.recv(1024)
# data = message
# while message:
#     message = s.recv(1024)
#     data += message
#
#     f.write(data)
f.close()
print("Successfully got file")
print("Connection closed")
s.close()


# from socket import *
# import sys
#
# HOST = "localhost"
# PORT = int(sys.argv[1])
#
# s = socket(AF_INET,SOCK_STREAM)
# s.connect((HOST, PORT))
#
# file_name = input('Insert file name')
# print(file_name)
# s.send(file_name.encode())
# f = open(file_name,"wb") #victor says its wb?
#
# message = s.recv(1024)
# data = message
# while message:
#     message = s.recv(1024)
#     data += message
#
# f.write(data)
# f.close()
# s.close()
