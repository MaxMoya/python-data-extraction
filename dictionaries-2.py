mail = open('mbox-short.txt')
count = dict()
list = list()
for lines in mail:
    if not lines.startswith('From '):
        continue
    lines = lines.split()
    time = lines[5]
    hr = time[:2]
    if hr not in count:
        count[hr] = 1
    else:
        count[hr] = count[hr] + 1

for key, val in count.items():
    list.append( (key, val) )

list.sort()

for key, val in list:
    print(key, val)


