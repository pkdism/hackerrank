import re
p = r"(?<=.)(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})(?=.)"

for _ in range(int(input())):
    s = input()
    r = re.findall(p, s, re.IGNORECASE)
    if r:
        for m in r:
            print(m)
