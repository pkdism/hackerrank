import re
s = input()
c = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
v = 'AEIOUaeiou'
res = re.findall(r'(?<=[%s])([%s]{2,})(?=[%s])'%(c,v,c), s)
if len(res) != 0:
    for i in res:
        print(i)
else:
    print(-1)
