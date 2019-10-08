from collections import deque

t = int(input())

for _ in range(t):
    cur_pile = 10000000000000
    n = int(input())
    dq = deque(list(map(int, input().split())))
    res = 'Yes'

    while len(dq) > 0:
        left = dq[0]
        right = dq[-1]

        if left > cur_pile or right > cur_pile:
            res = 'No'
            break

        cur_pile = max(left, right)

        if left > right:
            dq.popleft()
        elif right > left:
            dq.pop()
        else:
            dq.pop()
            if len(dq) > 0:
                dq.popleft()
    print(res)
