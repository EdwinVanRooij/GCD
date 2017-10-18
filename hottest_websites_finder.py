import re

pattern = re.compile("\s/([^\s]+)")
f.groupBy(lambda x: pattern.search(x).group(1) if pattern.search(x) != None else "").map(lambda x: (x[0], len(x[1]))).takeOrdered(10, lambda x: -x[1])
