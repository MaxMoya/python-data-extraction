import re
l = list()
han = open('regex_sum_1612090.txt')
for x in han :
    y = re.findall('[0-9]+', x)
    if not len(y) < 1 :
        l.append(y)
flatlist = sum(l, [])
flatlist = [int(i) for i in flatlist]
print(sum(flatlist))
