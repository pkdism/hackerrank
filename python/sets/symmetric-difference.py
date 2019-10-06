m = int(input())
am = set(list(map(int, input().split())))
n = int(input())
an = set(list(map(int, input().split())))

un = am.union(an)
ins = am.intersection(an)

res = un.difference(ins)
for i in sorted(res):
    print(i)
