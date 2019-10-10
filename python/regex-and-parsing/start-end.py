import re
s = input()
k = input()

pattern = re.compile(k)

m = re.search(pattern, s)

if not m:
    print(tuple([-1, -1]))
else:
    while m:
        print(tuple([m.start(), m.end() - 1]))
        m = pattern.search(s, m.start()+1)
