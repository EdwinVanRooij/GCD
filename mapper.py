#!/usr/bin/env python3

import sys

for line in sys.stdin:

    data = line.strip().split("\t")

    date, time, store, item, cost, payment = data

    if len(data) == 6:
        # Now print out the data that will be passed to the reducer
        print("{0}\t{1}".format(store, cost))


# 2012-01-01	09:00	San Jose	Men's Clothing	214.05	Amex
# 2012-01-01	09:00	Fort Worth	Women's Clothing	153.57	Visa
# 2012-01-01	09:00	San Diego	Music	66.08	Cash
# 2012-01-01	09:00	Pittsburgh	Pet Supplies	493.51	Discover
# 2012-01-01	09:00	Omaha	Children's Clothing	235.63	MasterCard
# 2012-01-01	09:00	Stockton	Men's Clothing	247.18	MasterCard
# 2012-01-01	09:00	Austin	Cameras	379.6	Visa
# 2012-01-01	09:00	New York	Consumer Electronics	296.8	Cash
# 2012-01-01	09:00	Corpus Christi	Toys	25.38	Discover
# 2012-01-01	09:00	Fort Worth	Toys	213.88	Visa
