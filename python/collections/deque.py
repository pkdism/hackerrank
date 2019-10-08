from collections import deque
n = int(input())

dq = deque()

for _ in range(n):
    command = input().split()
    c = command[0]
    if c == 'append':
        dq.append(command[1])
    elif c == 'appendleft':
        dq.appendleft(command[1])
    elif c == 'pop':
        dq.pop()
    elif c == 'popleft':
        dq.popleft()
print(' '.join(map(str, dq)))
