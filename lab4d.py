#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(arg):
    # Returns the first five characters using [:5]
    return arg[:5]

def last_seven(arg):
    # Returns the last seven characters using negative indexing [-7:]
    return arg[-7:]

def middle_number(arg):
    # Convert the number to a string first, then slice the 2nd and 3rd chars
    # Index 1 is the 2nd char, index 3 is the stop point (exclusive)
    num_str = str(arg)
    return num_str[1:3]

def first_three_last_three(arg1, arg2):
    # Combines first three of arg1 and last three of arg2
    return arg1[:3] + arg2[-3:]


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
