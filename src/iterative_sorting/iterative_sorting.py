# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): 
        cur_index = i 
        smallest_index = cur_index 

        for j in range(i+1, len(arr)): #loop through items in array starting at i + 1 to the end
            if arr[j] < arr[smallest_index]: #if the value of j is smaller than the smallest index
                smallest_index = j # set the smallest index equal to j
        # TO-DO: swap
        if smallest_index: # it smallest index has been changed
            arr[smallest_index],arr[cur_index] = arr[cur_index], arr[smallest_index]
            # swap smallest index with the current index

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr)-1): # for i from the range of 0 to the length of the arr - 1
        swapped = False # swapped is set to false

        for j in range(0, len(arr)-1): # for j in the range of 0 to arr -1
            if arr[j] > arr[j+1]: # if the value at j is greater than the value at j + 1
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap j and j+1
                swapped = True # and set swapped to true
        if(swapped != True): # if swapped is not true
            break # stop the loop
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr