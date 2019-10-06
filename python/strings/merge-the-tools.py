def merge_the_tools(string, k):
    l = len(string)
    for i in range(0,l,k):
        sub = string[i:(i+k)]
        small_hash = {}
        for j in sub:
            small_hash[j] = 1
        res = ''
        for j in sub:
            if small_hash[j] == 1:
                res += j
                small_hash[j] = 0
        print(res)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
