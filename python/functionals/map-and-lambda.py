cube = lambda x: pow(x, 3)

def fibonacci(n):
    l = [0, 1]
    if n <= 2:
        return l[0:n]
    for i in range(2, n):
        l.append(l[i-1] + l[i-2])
    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
