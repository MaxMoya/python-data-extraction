mail = open('mbox-short.txt')
count = dict()
list = list()
for lines in mail:
    if not lines.startswith('From '):
        continue
    lines = lines.split()
    adr = lines[1]
    if adr not in count:
        count[adr] = 1
    else :
        count[adr] = count[adr] + 1

for sent, email in count.items() :
    list.append( (email, sent) )

list.sort(reverse=True)

print(list[0])