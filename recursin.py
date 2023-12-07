
def factorial_calc(value):
    # factorial of 0 is 1 as we know
    if value==0:
        return 1
    return value*factorial_calc(value-1)



def calc_permutations(str):
  result = []
  if len(str) == 1:
    return str
  else:
    for i,val in enumerate(str):
      for res in calc_permutations(str[:i] + str[i+1:]):
        result += [val + res]
  return result


if __name__ == '__main__':
    num=5
    print("the factorial vlaue of of num is:",factorial_calc(num))

    temp="abcve"
    print(calc_permutations(temp))