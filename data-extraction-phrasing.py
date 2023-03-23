#Reading a file and looking for specific phasing
file = input('File Name: ')
try:
    handle = open(file)
except:
    print('Seriously, dude...', file.lstrip(), '?')
    exit()
for line in handle:
    if line.startswith('X-DSPAM-Confidence:'):
        line2 = line
        print(line2)