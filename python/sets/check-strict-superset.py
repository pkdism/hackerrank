a = set(input().split())

n = int(input())

c = 0
for i in range(n):
    s = set(input().split())
    c += (len(s.union(a)) == len(a) and len(s) != len(a))

print(c == n)
