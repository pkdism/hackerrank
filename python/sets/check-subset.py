t = int(input())

for i in range(t):
    na = int(input())
    a = set(list(map(int, input().split())))

    nb = int(input())
    b = set(list(map(int, input().split())))

    u = a.union(b)
    ins = a.intersection(b)

    print(len(u) == len(b))
