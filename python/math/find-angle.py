import math

ab = int(input())
bc = int(input())

ac = pow(pow(ab, 2) + pow(bc, 2), 0.5)

mb = math.sin(math.atan(ab/bc))*bc

rad = math.acos(mb/bc)

deg = math.degrees(rad)

deg = 90 - deg

res = ''
if deg%1.0 >= 0.5:
    res = str(math.ceil(deg)) + '°'
else:
    res = str(math.floor(deg)) + '°'

print(res)
