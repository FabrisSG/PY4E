'''In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers.
 There are 71 values and the sum ends with 726'''

import re
numeros = list()
hand = open('regex-sum.txt')
for line in hand:
    y = re.findall('[0-9]+', line)
    if len(y) > 0:
        for i in y:
            i = int(i)
            numeros.append(i)

print(sum(numeros))
