import string
mail = open('sample_10_3.txt')
count = dict()
for lines in mail:
    lines = lines.strip()
    lines = lines.translate(lines.maketrans('', '', string.punctuation))
    lines = lines.lower()
    for letters in lines:
        count[letters] = count.get(letters, 0) + 1

list = list()

for k, v in count.items():
    list.append((k,v))
    list.sort()
for a in list:
    print(a)