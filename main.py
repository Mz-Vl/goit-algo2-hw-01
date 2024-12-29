def find_min_max(arr):
    """
    Find the minimum and maximum elements in the array.

    Args:
        arr (list): The input array.

    Returns:
        tuple: A tuple containing the minimum and maximum elements.
    """
    if len(arr) == 1:
        return arr[0], arr[0]

    if len(arr) == 2:
        return min(arr[0], arr[1]), max(arr[0], arr[1])

    mid = len(arr) // 2
    left_min_max = find_min_max(arr[:mid])
    right_min_max = find_min_max(arr[mid:])

    overall_min = min(left_min_max[0], right_min_max[0])
    overall_max = max(left_min_max[1], right_min_max[1])

    return overall_min, overall_max

array = [3, 1, 7, 9, 2, 5]
print(find_min_max(array))
