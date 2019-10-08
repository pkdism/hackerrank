from collections import namedtuple
n = int(input())
students = namedtuple('students', input())
print(sum([int(students(*input().split()).MARKS) for _ in range(n)])/(n))

# for i in range(n):
#     s = students(*input().split())
#     marks.append(int(s.MARKS))

# print(sum(marks)/len(marks))
