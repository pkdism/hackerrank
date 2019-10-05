def swap_case(s):
    diff = ord('a') - ord('A')

    res = ""
    for i in s:
        val = i
        if i >= 'a' and i <= 'z':
            val = chr(ord(i) - diff)
        elif i >= 'A' and i <= 'Z':
            val = chr(ord(i) + diff)
        res += val

    return(res)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
