def minion_game(string):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    vid = []
    cid = []
    l = len(string)
    for i in range(l):
        if string[i] in vowels:
            vid.append(i)
        else:
            cid.append(i)
    kevin = 0
    stuart = 0
    for i in vid:
        kevin += (l - i)
    for i in cid:
        stuart += (l - i)
    if stuart < kevin:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
