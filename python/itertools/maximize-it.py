from itertools import product
k, m = map(int, input().split())
nums = []
for i in range(k):
    l = list(map(int, input().split()))
    nums.append(l[1:])

res = 0
prods = list(product(*nums))

for one_prod in prods:
    temp = sum([x*x for x in one_prod])%m
    if temp > res:
        res = temp

print(res)
