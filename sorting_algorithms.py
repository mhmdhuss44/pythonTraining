
# bubble sort algorithm:
def bubble_sort(arr):
    # bubble sort loop on each two elemnts and swap if needed
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

# merge sort algorithm
def merge_sort(arr):
    if len(arr)<2:
        return arr
    else:
        med=len(arr)//2
        first=merge_sort(arr[:med])
        second=merge_sort(arr[med:])
        return merge(first,second)

def merge(first,second):
    result=[]
    i=0
    j=0
    while i<len(first) and j<len(second):
        if first[i]<=second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1


    while i<len(first) :
        result.append(first[i])
        i+=1
    while j<len(second):
        result.append(second[j])
        j+=1
    return result


# quick sort algorithm in python

def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        first=[x for x in arr[1:] if x<pivot]
        second=[x for x in arr[1:] if x>= pivot]
        return quick_sort(first)+[pivot]+quick_sort(second)


if __name__ == '__main__':
    arr=[3,4,1,2,8,9,25,11,14,12,0,-5]
    # bubble_sort(arr)
    # print(arr)

    # result = merge_sort(arr)
    # print(result)
    
    result=quick_sort(arr)
    print(result)
