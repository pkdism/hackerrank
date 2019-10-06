def print_line(l, letters, size):
    characters = '-'.join(letters[0:(l + 1)])
    reverse_characters = ''.join([i for i in reversed(characters[:-1])])
    all_characters = characters + reverse_characters
    print(all_characters.center(size*4 - 3, '-'))

def print_rangoli(size):
    letters = [chr(i) for i in range(ord('a') + size - 1, ord('a') - 1, -1)]

    for i in range(size):
        print_line(i, letters, size)

    for i in range(size - 2, -1, -1):
        print_line(i, letters, size)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
