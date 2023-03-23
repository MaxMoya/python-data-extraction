#key = dict()
#file = open('words.txt')
#for lines in file:
   # lines = lines.split()
    #for word in lines :
    #    if word not in key:
   #         key[word] = 1
  #      else:
 #           key[word] = key[word] + 1
#print(key)

key = dict()
file = open('words.txt')
for lines in file:
    lines = lines.split()
    for word in lines :
        key[word] = key.get(word,0) + 1
print(key)