def mutate_string(string, position, character):
    if position == (len(string) - 1):
        res = string[:position] + character
    elif position == 0:
        res = character + string[(position+1):]
    else:
        res = string[:position] + character + string[(position+1):]
    return res

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
