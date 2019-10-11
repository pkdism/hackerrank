import email.utils
import re
n = int(input())
pattern = r"^[a-zA-Z](\w|-|\.|_])+@[a-zA-Z]+\.[a-zA-Z]{1,3}$"

for _ in range(n):
    s = input()
    e = email.utils.parseaddr(s)
    r = re.match(pattern, e[1])
    if r:
        print(email.utils.formataddr(email.utils.parseaddr(s)))
