from itertools import combinations

s = input().split()

word = s[0]
k = int(s[1])

for j in range(1, k+1, 1):
    for i in combinations(sorted(word), j):
        print(''.join(i))
