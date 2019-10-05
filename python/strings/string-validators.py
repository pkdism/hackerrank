if __name__ == '__main__':
    s = input()
    is_alnum = 0
    is_alpha = 0
    is_digit = 0
    is_lower = 0
    is_upper = 0

    for i in s:
        is_alnum += i.isalnum()
        is_alpha += i.isalpha()
        is_digit += i.isdigit()
        is_lower += i.islower()
        is_upper += i.isupper()

    print(is_alnum > 0)
    print(is_alpha > 0)
    print(is_digit > 0)
    print(is_lower > 0)
    print(is_upper > 0)
