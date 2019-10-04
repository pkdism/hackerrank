n = int(input())
a = [int(x) for x in input().split()]

m = max(a)
res = -1000
for i in a:
    if  i != m and i > res:
        res = i
print(res)    
