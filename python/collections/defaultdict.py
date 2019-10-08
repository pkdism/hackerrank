from collections import defaultdict

dd = defaultdict(list)

n, m = map(int, input().split())

for i in range(n):
    dd[input()].append(i+1)

for i in range(m):
    s = input()
    if len(dd[s]) > 0:
        print(' '.join(map(str, dd[s])))
    else:
        print(-1)
