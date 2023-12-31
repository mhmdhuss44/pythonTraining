
# bubble sort algorithm:
def bubble_sort(arr):
    # bubble sort loop on each two elemnts and swap if needed
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


# Time Complexity: O(n^2)
# Explanation: nested loops result in a quadratic time complexity becuase
# the algorithm compares and swaps elements for each pair .
# In the worst case  it takes n * (n-1) time


# merge sort algorithm
def merge_sort(arr):
    if len(arr)<2:
        return arr
    else:
        med=len(arr)//2
        first=merge_sort(arr[:med])
        second=merge_sort(arr[med:])
        return merge(first,second)

    # Time Complexity: O(n log n)
    # Explanation: Merge sort keep dividing the array into two equal parts recursively - we get logn from here
    # and then merges the sorted parts (using the merge function) it takes O(n)


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

# Time Complexity: O(n^2) (worst case if bad pivot ), O(n log n) (average case)
# Explanation: Quick sort time complexity depends on the choice of the pivot:
# In the worst case, where the pivot is poorly chosen (for example the smallest or largest element),
# the array is divided into not close in size partitions resulting in a quadratic time complexity...
# On average, with a good pivot selection (for example always geeting the median), the time complexity is O(n log n).

if __name__ == '__main__':
    arr=[3,4,1,2,8,9,25,11,14,12,0,-5]
    # bubble_sort(arr)
    # print(arr)

    # result = merge_sort(arr)
    # print(result)
    
    result=quick_sort(arr)
    print(result)
