# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): # for items in the range between 0 and one less than the length of the array (because the first item is already sorted?)

        cur_index = i # the selected item 

        smallest_index = cur_index # starts out as cur_index until it finds an item that is smaller

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        #need a second for loop
        for i in range(cur_index, len(arr)): #I need a loop that compares the cur_index to each other item to the right of cur_index
            if i < smallest_index:
                smallest_index = i
        # TO-DO: swap
        cur_index = smallest_index



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr