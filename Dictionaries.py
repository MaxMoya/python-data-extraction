cnt = dict()
x = input('Enter a file name:')
fx = open(x)
for y in fx:
    if not y.startswith('From '):
        continue
    z = y.split()
    a = z[1]
    cnt[a] = cnt.get(a,0) + 1

cnt2 = None
email = None
for word,count in cnt.items():
    if cnt2 is None or count > cnt2:
        cnt2 = count
        email = word
print(email, cnt2)
