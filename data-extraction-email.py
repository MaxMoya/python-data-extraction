mail = open('mbox-short.txt')
rl = dict()
for a in mail:
    if not a.startswith('From '):
        continue
    a = a.split()
    b = a[1]
    if b not in rl:
        rl[b] = 1
    else:
        rl[b] += 1

print(rl)

large = None
for v in rl:
    if large is None or rl[v] > large:
        large = v

print('Maximum:', large[v])