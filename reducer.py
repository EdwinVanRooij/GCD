import sys

highestSale = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data
    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", highestSale)
        oldKey = thisKey
        highestSale = 0

    oldKey = thisKey
    if float(thisSale) > highestSale:
        highestSale = float(thisSale)

if oldKey is not None:
    print(oldKey, "\t", highestSale)
