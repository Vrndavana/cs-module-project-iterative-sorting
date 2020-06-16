def linear_search(arr, target):
    # Your code here
    for a in range(0, len(arr)):
        if arr[a] == target:
            return a
    return -1   # not found
# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # set boundaries for low and high marks to search
    lo = 0
    hi = len(arr)
    # whle low and high do not overlap...
    while lo < hi:
        # check the midpoint
        mid = (lo + hi) // 2
        # if its equal, return true
        if arr[mid] == target:
            return mid
        # else, if target is smaller
        elif target < arr[mid]:
            # set hi to midpoint value
            hi = mid
        #else if taret is bigger
        else:
            #set the low to midpoint value
            lo = mid + 1
    return -1  # not found