import socket

# Source help: https://www.geeksforgeeks.org/socket-programming-python/
url = "gaia.cs.umass.edu"
PORT = 80

ip = socket.gethostbyname(url)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("client connecting to:", ip)
s.connect((url,PORT))


#Source for help: https://www.geeks3d.com/hacklab/20190110/python-3-simple-http-request-with-the-socket-module/
request = "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost: gaia.cs.umass.edu\r\n\r\n"
s.send(request.encode())

y = s.recv(4096)
x = y
while len(y) > 0:
     y = s.recv(4096)
     x += y

response = str(x)

print(response.replace('\\r','').replace('\\n','\n'))
