n = int(input())

s = input()

t = tuple([int(x) for x in s.split()])
print(hash(t))
