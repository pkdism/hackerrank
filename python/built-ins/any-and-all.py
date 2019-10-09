n = int(input())
ints = list(map(int, input().split()))

all_positive = all([i >= 0 for i in ints])
any_palindrome = any([int(''.join(reversed(str(abs(i))))) == i for i in ints])

print(all_positive and any_palindrome)
