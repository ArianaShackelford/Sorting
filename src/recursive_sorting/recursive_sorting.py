# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0 # represents temporary storage and index of merged_arr
    b = 0
    # compare the first i in each array and add the smaller to the result
    for i in range(0, elements): #for each element in the array from 0 to elements (length of both arrays together)
        if a >= len(arrA):  # if a is larger or == than the length of arrA
            merged_arr[i] = arrB[b] #set merged_arr at i to arrB at b
            b += 1 # incrament a 
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]: # if the next element in arrA is smaller add to merged_arr
            merged_arr[i] = arrA[a]
            a += 1
        else: # if a is not smaller than b must be
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # base - if the array is empty or the length of 1 return
    if len(arr) > 1: 
        arrA = merge_sort(arr[0 : len(arr)//2])
        arrB = merge_sort(arr[len(arr)//2 : ])
        arr = merge(arrA, arrB)
        return arr

    else:
        return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
