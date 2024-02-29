def longest_consecutive_sequence(nums):
    set_seq = set(nums)  # Convert the list to a set
    length = 0  # This will store the maximum length of consecutive sequence found

    for num in set_seq:
        # Find the start of a sequence
        if num - 1 not in set_seq:
            current_length = 1
            current_num = num
            while current_num + 1 in set_seq:
                current_num += 1
                current_length += 1

            length = max(length, current_length)  # Update the max length if current is longer

    return length


print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))

"""
    EXPECTED OUTPUT:
    ----------------
    4

"""