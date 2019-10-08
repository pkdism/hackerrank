from collections import OrderedDict

n = int(input())

items = OrderedDict()

for i in range(n):
    thing = input().split()
    name = ' '.join(thing[:-1])
    price = thing[-1]
    items[name] = items.get(name, 0) + int(price)

for name,price in items.items():
    print(name, price, sep = ' ')
