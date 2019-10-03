def print_weird(is_weird):
    if is_weird == True:
        print("Weird")
    else:
        print("Not Weird")

n = int(input())

if n%2 == 1:
    print_weird(True)
elif n%2 == 0 and n >= 2 and n <= 5:
    print_weird(False)
elif n%2 == 0 and n >= 6 and n <= 20:
    print_weird(True)
elif n%2 == 0 and n > 20:
    print_weird(False)
