import sys

total=0
oldKey=None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisNum = data_mapped

    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", total)
        total = 0

    oldKey = thisKey
    total += float(thisNum)

if oldKey != None:
    print(oldKey, "\t", total)
