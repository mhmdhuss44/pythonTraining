
# a function to reverese a string in place
def str_reverse(str):
    arr_temp=list(str)
    first=0
    last=len(arr_temp)-1
    while first<last:
        arr_temp[first],arr_temp[last]=arr_temp[last],arr_temp[first]
        first+=1
        last-=1
#  turning array back into string
    str=''.join(arr_temp)
    return str



# function to find the max/min in an array
def max_min_find(arr):
    # we could use an already built in functions
    max_element=max(arr)
    min_element=min(arr)
    return max_element,min_element


# a function to remove duplicates from a sorted array
# we use a two pointer algorithm !
def dublicates_remove(arr):
    # arr=[5,5,5,7,7,8,8]
    pos=0
    last=1
    for i in range(0,len(arr)):
        if arr[i]==arr[pos]:
            continue
        else:
            pos=i
            arr[last]=arr[i]
            last+=1
    return arr[:last]


if __name__ == '__main__':

    # test for the first
    wow="mhms5555x"
    print(str_reverse(wow))

    # test for the second
    arr=[2,3,6,7,99,5]
    x,y=max_min_find(arr)
    print(x,y)

    # test for the third
    temp=[5,5,5,8,8,8,9,9,9,10,10,10,15,15,15,18,18,18,25,26,27]
    print(dublicates_remove(temp))