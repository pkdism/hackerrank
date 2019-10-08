from collections import Counter
x = int(input())
sizes = map(int, input().split())

cn = Counter(sizes)
earned = 0
n = int(input())
for i in range(n):
    sz, price = map(int, input().split())
    if cn[sz] > 0:
        cn[sz] -= 1
        earned += price

print(earned)
