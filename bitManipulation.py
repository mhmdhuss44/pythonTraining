
def is_even(number):
    # we just ise & and it will change our number to binary
    return (number & 1) == 0

def counteSet_bits(num):
    count = 0
    while num:
        # this will check is right most number if its 0 or 1
        count += num & 1
        # we shift to the next digit
        num >>= 1
    return count

if __name__ == '__main__':
    num = 13
    if is_even(num):
        print(num,"is even.")
    else:
        print(num,"is odd.")

    number = 26  # You can replace this with any integer
    result = counteSet_bits(number)
    print("Number of set bits is",result)
