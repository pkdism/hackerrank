def print_formatted(number):
    l = len(bin(number)) - 2
    for i in range(1, number + 1):
        binary = bin(i)[2:]
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:]
        print('{num: >{wid}}'.format(num = i, wid = l),
        '{num: >{wid}}'.format(num = octal, wid = l),
        '{num: >{wid}}'.format(num = hexadecimal, wid = l).upper(),
        '{num: >{wid}}'.format(num = binary, wid = l))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
