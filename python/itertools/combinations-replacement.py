from itertools import combinations_with_replacement

s = input().split()

word = s[0]
k = int(s[1])


for i in combinations_with_replacement(sorted(word), k):
    print(''.join(i))
