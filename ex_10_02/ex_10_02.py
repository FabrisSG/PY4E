name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
contadores = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith("From") or line.find("2008") == -1:
        continue
    line = line.split()
    t = line[5]
    delimiter = ":"
    s = t.split(delimiter)
    numeros = s[0]
    for numero in numeros:
        if numero not in contadores:
            contadores[numero] = 1
        else:
            contadores[numero] += 1


lst = list()
for key, value in list(contadores.items()):
    lst.append((key, value))

lst.sort(reverse=True)

for key, value in lst[:10]:
    print(key, value)
