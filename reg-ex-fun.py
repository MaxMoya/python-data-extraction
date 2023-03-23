import re
f = open('regex_sum_1612090.txt')
print(sum([int[i] for i in re.findall('[0-9]+', f.read())])) 
#'regex_sum_1612090.txt'.read()