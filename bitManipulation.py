
def is_even(number):
    # we just ise & and it will change our number to binary
    return (number & 1) == 0

if __name__ == '__main__':
    num = 13
    if is_even(num):
        print(num,"is even.")
    else:
        print(num,"is odd.")
