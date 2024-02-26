def subarray_sum(nums, target):
    running_sum = {0: -1}  # Base case initialization
    total = 0
    for index, value in enumerate(nums):
        total += value
        if (total - target) in running_sum:  # Check if the complement sum exists
            start_index = running_sum[total - target] + 1  # Start index of subarray
            return [start_index, index]  # Return indices of the subarray
        running_sum[total] = index  # Store running sum and its index

        # Handle case where the running sum itself matches the target
        if total == target:
            return [0, index]  # Subarray starts from the beginning

    return []  # Return empty list if no subarray found


nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))

nums = [-1, 2, 3, -4, 5]
target = 0
print(subarray_sum(nums, target))

nums = [2, 3, 4, 5, 6]
target = 3
print(subarray_sum(nums, target))

nums = []
target = 0
print(subarray_sum(nums, target))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
