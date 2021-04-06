# Time complexity = O(n)
# Space complexity = O(1)

def linear_search(list, target):
    """ 
    Returns the index position of the target if found, else returns None
    """
    # 1st way of writing function

    for i in range(0, len(list)):     # len(list) = O(1) - constant runtime complexity
        if list[i] == target:
            return i
    return None

    # 2nd way of writing function using enumerate 

    # for index, value in enumerate(list):
    #     if value == target:
    #         return index
    # return -1

def verify(index):
    if index is not None:
        print("Target found at index:",index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
verify(result)


