import re
n = int(input())
pattern = r"^[789]([0-9]){9}$"
for _ in range(n):
    if re.match(pattern, input()):
        print("YES")
    else:
        print("NO")
