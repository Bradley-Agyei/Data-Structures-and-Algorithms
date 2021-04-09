# Time complexity for Binary Search = O(log n)
# List has to be sorted 

def binary_search(list, target):
    # points to first element in the list
    first = 0                           # O(1) - assigning values

    #points to last element in the list
    last = len(list) - 1

    while first <= last:                # while loop makes algorithm O(log n)
        midpoint = (first + last)//2    # Floor division, rounds down to whole number. O(1) run time 

        if list[midpoint] == target: 
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1  
        else:
            last = midpoint - 1 
    return None 

def verify(index):
    if index is not None:
        print("Target found at index:",index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 6)
verify(result)