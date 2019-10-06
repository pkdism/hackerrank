n = int(input())
a = set(list(map(int, input().split())))

m = int(input())
for i in range(m):
    oper = input().split()
    new = set(list(map(int, input().split())))
    if oper[0] == 'update':
        a.update(new)
    elif oper[0] == 'intersection_update':
        a.intersection_update(new)
    elif oper[0] == 'difference_update':
        a.difference_update(new)
    elif oper[0] == 'symmetric_difference_update':
        a.symmetric_difference_update(new)

print(sum(a))
    
