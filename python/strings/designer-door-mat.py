# 0
# - m-3*(i+1)
#
# mp = ".|."
# len(mp) = 3*(i+1)
#
#
# len(dash) = m-3*(i+1)
#
# if i == n//2
# len(dash) = m-7

s = [int(x) for x in input().split()]
n, m = int(s[0]), int(s[1])

mp = ".|."
dash = "-"
for i in range(n):
    if i == n//2:
        l_dash = (m-7)//2
        print(dash*l_dash + 'WELCOME' + dash*l_dash)
    else:
        if i > (n//2):
            i = n - i - 1
        l_mp = 2*i+1
        l_dash = m - 3*l_mp
        print(dash*(l_dash//2) + l_mp*mp + dash*(l_dash//2))
