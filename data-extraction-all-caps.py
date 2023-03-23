#Reading a file in all caps
file = input('File Name: ')
handle = open(file)
for line in handle:
    lines = line.upper()
    lines.strip()
    print(lines) 