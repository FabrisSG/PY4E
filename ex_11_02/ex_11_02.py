import re
nombre = input("Enter file:")
if len(nombre) < 1:
    nombre = "regex_sum_1219235.txt"
handle = open(nombre)

total = 0
for linea in handle:
    n = re.findall('[0-9]+', linea)
    y = len(n)
    for i in range(y):
        total = total + int(n[i])
print(total)
