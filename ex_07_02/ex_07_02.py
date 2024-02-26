fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
         continue
    s = float(line[20:])
    total = total + s
    count = count + 1
average = total / count
print("Average spam confidence:", average)
