n = int(input())
e = set(list(map(int, input().split())))

b = int(input())
f = set(list(map(int, input().split())))

print(len(e.symmetric_difference(f)))