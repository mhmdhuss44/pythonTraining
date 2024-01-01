
def factorial_calc(value):
    # factorial of 0 is 1 as we know
    if value==0:
        return 1
    return value*factorial_calc(value-1)

# Space Complexity: O(n)
# Explanation: The space complexity of is determined by the depth of the stack in recursion
# and in the Worst Case Scene we have to go n times! (because we reduce 1 each time until we get to 0)





def calc_permutations(str):
  result = []
  if len(str) == 1:
    return str
  else:
    for i,val in enumerate(str):
      for res in calc_permutations(str[:i] + str[i+1:]):
        result += [val + res]
  return result

# Space Complexity: O(n!)
# Explanation: The space complexity of the function is determined
# by the number of permutations , and we know that the number of permuatations of a string
# of len n is n! and each one takes a recursive call , so we have n! stack calls


if __name__ == '__main__':
    num=5
    print("the factorial vlaue of of num is:",factorial_calc(num))

    temp="abcve"
    print(calc_permutations(temp))