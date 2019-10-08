from itertools import combinations

n = int(input())
s = input().split()
k = int(input())
c = 0
for comb in combinations(s, k):
    if 'a' in comb:
        c += 1
print('%.3f'%(c/len(list(combinations(s, k)))))
