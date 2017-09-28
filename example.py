#!/usr/bin/env python
import mincemeat
import glob

# data = ["Humpty Dumpty sat on a wall",
#         "Humpty Dumpty had a great fall",
#         "All the King's horses and all the King's men",
#         "Couldn't put Humpty together again",
#         ]

all_files = glob.glob('Gutenberg/Gutenberg Small/*.*')
# all_files = glob.glob('Gutenberg/TestDir/*.*')


def file_contents(file_name):
    with open(file_name, encoding="ISO-8859-1") as f:
        # f = open(file_name, encoding="ISO-8859-1")
        return f.read()


data = dict((file_name, file_contents(file_name)) for file_name in all_files)


def mapfn(k, v):
    for w in v.split():
        yield w, 1


def reducefn(k, vs):
    result = 0
    for v in vs:
        result += v
    return result


s = mincemeat.Server()

# The data source can be any dictionary-like object
s.datasource = data
# print("Datasource:", data)
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print(results)

# # !/usr/bin/env python
# import mincemeat
#
# data = ["Humpty Dumpty sat on a wall",
#         "Humpty Dumpty had a great fall",
#         "All the King's horses and all the King's men",
#         "Couldn't put Humpty together again",
#         ]
#
# def mapfn(k, v):
#     for w in v.split():
#         yield w, 1
#
# def reducefn(k, vs):
#     result = 0
#     for v in vs:
#         result += v
#     return result
#
# s = mincemeat.Server()
#
# # The data source can be any dictionary-like object
# s.datasource = dict(enumerate(data))
# print(s.datasource)
# s.mapfn = mapfn
# s.reducefn = reducefn
#
# results = s.run_server(password="changeme")
# print(results)
