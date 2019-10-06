n = int(input())
s = set(map(int, input().split()))

n_commands = int(input())
for i in range(n_commands):
    oper = input().split()
    if oper[0] == 'pop':
        s.pop()
    elif oper[0] == 'remove':
        s.remove(int(oper[1]))
    elif oper[0] == 'discard':
        s.discard(int(oper[1]))
print(sum(s))
