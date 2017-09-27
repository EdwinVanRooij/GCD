import sys

totalSales = 0
totalAmount = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisAmount, thisSale = data
    # if oldKey and oldKey != thisKey:
    #     print("{}\t{}\t{}".format(oldKey, totalAmount, totalSales))
    #     oldKey = thisKey
    #     totalSales = 0
    #     totalAmount = 0

    # oldKey = thisKey
    totalAmount += int(thisAmount)
    totalSales += float(thisSale)

# if oldKey is not None:
print("{}\t{}\t{}".format(oldKey, totalAmount, totalSales))
