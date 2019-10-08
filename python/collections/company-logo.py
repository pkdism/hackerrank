from collections import OrderedDict

s = ''.join(sorted(input()))

od = OrderedDict()

for i in s:
    od[i] = od.get(i, 0) + 1

sorted_od = sorted(od.items(), key = lambda item: item[1], reverse = True)[0:3]

for item in sorted_od:
    print(item[0], item[1], sep = ' ')
