n = int(input())

marks = []
first_min = 100000
second_min = 100000
for i in range(n):
    name = input()
    value = float(input())
    marks.append([name, value])
    if value < first_min:
        first_min = value

for i in range(n):
    name = marks[i][0]
    value = marks[i][1]
    if value != first_min and value < second_min:
        second_min = value

names = []
for i in range(n):
    if marks[i][1] == second_min:
        names.append(marks[i][0])

for i in sorted(names):
    print(i)
