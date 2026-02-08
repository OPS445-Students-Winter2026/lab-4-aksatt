#!/usr/bin/env python3
# Author ID: 184240232

def is_digits(sobj):
    """
    Checks if a string consists only of numeric digits.
    Returns True if all characters are digits, False otherwise.
    """
    for char in sobj:
        # If the character is not found in the string of digits, it's invalid
        if char not in '0123456789':
            return False
    # If we made it through the loop, all characters were digits
    return True

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')
