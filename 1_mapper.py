import sys

for line in sys.stdin:
    start=line.find("GET ")
    end=line.find("HTTP")
    match=line[start+4:end]
    print("{}\t{}".format(match, 1))
