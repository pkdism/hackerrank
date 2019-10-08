from itertools import groupby

s = input()

for k, g in groupby(s):
    print(tuple([len(list(g)), int(k)]), end = ' ')
