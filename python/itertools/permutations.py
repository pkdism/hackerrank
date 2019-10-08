from itertools import permutations

s = input().split()

word = s[0]
k = int(s[1])

for i in permutations(sorted(word), k):
    print(''.join(i))
