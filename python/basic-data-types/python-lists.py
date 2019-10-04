n = int(input())
l = []
for i in range(n):
    command = input().split()
    c = command[0]
    if len(command) == 3:
        index = int(command[1])
        value = int(command[2])
    if len(command) == 2:
        value = int(command[1])
    if c == 'insert':
        l.insert(index, value)
    elif c == 'print':
        print(l)
    elif c == 'remove':
        l.remove(value)
    elif c == 'append':
        l.append(value)
    elif c == 'sort':
        l.sort()
    elif c == 'pop':
        l.pop()
    elif c == 'reverse':
        l.reverse()
