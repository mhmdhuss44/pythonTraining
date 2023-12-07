from bisect import bisect, bisect_right


def linear_search(value,arr):
    if value in arr:
        return arr.index(value)
    else :
        return False

def binary_search(value,arr):
    low=0
    high=len(arr)-1
    while low<=high :
        med=(low+high)//2
        if value>arr[med]:
            low=med+1
        elif value<arr[med]:
            high=med-1
        else:
            return med
    return False



if __name__ == '__main__':
    arr=[2,8,9,4,3,6,7]
    pos=linear_search(19,arr)
    if pos is not False:
        print("the indix of the value in array is: ",pos)
    else:
        print("the value is not in the array ")

    second_arr=[1,2,3,8,9,15,16,17,18]
    # # note that there is a built in function for binary search too
    # temp=bisect_right(second_arr,2)
    # print(temp)

    temp=binary_search(18,second_arr)
    if temp is not False:
        print("the indix of the value in array is: ", temp)
    else:
        print("the value is not in the array ")