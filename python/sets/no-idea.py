n, m = map(int, input().split())

arr = list(map(int, input().split()))

a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

c = 0
for i in arr:
    if i in a:
        c += 1
    elif i in b:
        c -= 1
print(c)
