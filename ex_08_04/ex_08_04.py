fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    palabras = line.split()
    for palabra in palabras:
        if palabra in lst:
            continue
        lst.append(palabra)
        lst.sort()
print(lst)
