import re
for _ in range(int(input())):
    n = input()
    print(bool(re.match('^\+[0-9]*\.[0-9]+$', n)) or bool(re.match('^[0-9]*\.[0-9]+$', n) or bool(re.match('^\-[0-9]*\.[0-9]+$', n))))
