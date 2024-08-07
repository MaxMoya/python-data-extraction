import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input('Enter URL: ')
host = url.split('/')
host = host[2]
port = 80
count = 0

try:
    mysock.connect((host, port))
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
except:
    print('Please enter valid URL')
    exit()

data = mysock.recv(3000)
data1 = data.decode()
print(data1)

while True:
    data2 = mysock.recv(1024)
    if len(data2) < 1:
        break
    count = count + len(data2)
print(count)


mysock.close()
