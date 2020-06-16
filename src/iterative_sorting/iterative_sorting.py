# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # Your code here
        if cur_index != smallest_index:
            value = arr[smallest_index]
            arr.remove(value)
            arr.insert(cur_index, value)
    return arr
# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swaps = True
    while swaps:
        swaps = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps = True
    return arr