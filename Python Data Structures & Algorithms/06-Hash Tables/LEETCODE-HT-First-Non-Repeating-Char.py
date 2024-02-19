def first_non_repeating_char(string):
    char_dict = {}
    for character in string:
        char_dict[character] = char_dict.get(character, 0) + 1

    for character in string:
        if char_dict[character] == 1:
            return character
    return None


print(first_non_repeating_char('leetcode'))

print(first_non_repeating_char('hello'))

print(first_non_repeating_char('aabbcc'))

"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""