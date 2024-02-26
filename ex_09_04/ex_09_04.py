name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
di = dict()

for line in handle:
    if not 'From ' in line:
        continue
    else:
        words = line.split()
    emails = words[1]
    di[emails] = di.get(emails, 0) + 1

bigcount = None
bigword = None

for k,v in di.items():
    if bigcount is None or v > bigcount:
        bigword = k
        bigcount = v

print(bigword, bigcount)
