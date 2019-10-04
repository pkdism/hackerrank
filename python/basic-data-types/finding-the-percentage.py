n = int(input())

records = {}

for r in range(n):
    student = input().split()
    records[student[0]] = [float(i) for i in student[1:]]

name = input()
avg = sum(records[name])/3
print("{:.2f}".format(avg))
