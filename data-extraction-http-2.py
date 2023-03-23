import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/mbox.txt')
count = 0
data = fhand.read(3000)
print(data.decode())

while True:
    doc = fhand.read(3000)
    if len(doc) < 1:
        break
    count = count + len(doc)
print(count)

# Code: http://www.py4e.com/code3/urllib1.py
# url: httn(://data.pr4e.org/mbox.txt

