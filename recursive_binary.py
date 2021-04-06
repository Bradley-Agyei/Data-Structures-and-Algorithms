def recursive_binary(list, target, start=0, end=None):
    if end is None:
        end = len(list) - 1
    if start > end:
        return -1

    midpoint = (start + end) // 2

    if target == list[midpoint]:
        return midpoint
    else:
        if target < list[midpoint]:
            return recursive_binary(list, target, start, midpoint-1)
        else:
            return recursive_binary(list, target, midpoint+1, end)


def verify(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8]

result = recursive_binary(numbers, 3, 0, None)
verify(result)