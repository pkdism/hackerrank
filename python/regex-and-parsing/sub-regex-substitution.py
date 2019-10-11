import re

def replace(text):
    if text.group() == "&&":
        return "and"
    else:
        return "or"

n = int(input())
for _ in range(n):
    s = input()
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', replace, s))
