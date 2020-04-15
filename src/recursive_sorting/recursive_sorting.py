# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO
    # compare the first i in each array and add the smaller to the result
    while arrA and arrB > 0:
        if arrA[0]> arrB[0]:
            merged_arr.append(arrB[0])
            arrB.remove([0])
        else:
            merged_arr.append(arrA[0])
            arrA.remove([0])
    while arrA > elements:
        merged_arr.append(arrA[0])
        arrA.remove([0])
    while arrB > elements:
        merged_arr.append(arrB[0])
        arrB.remove([0])

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # base - if the array is empty or the length of 1 return
    # length = len(arr)
    if len(arr) <= 1: #this is not working and causeing infinite loop
        return arr
    #split the array in half
    # arrA = arr[0, :int(length/2+1)]
    # arrB = arr[:int(length/2 + 1), :int(length)
    else:
        arrA, arrB = arr[:len(arr)//2], arr[len(arr)//2 + 1:]
        #sort each half
        arrA = merge_sort(arrA)
        arrB = merge_sort(arrB)

    return merge(arrA, arrB)


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
