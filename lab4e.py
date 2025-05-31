#!/usr/bin/env python3
# The purpose of this script is to define a function called is_digits(), 
# which takes a string object as its argument and return True if all the characters in the string are all digits, 
# i.e 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9; return False if any one of the characters is not a digit.
#Author Leung Wai Rene Chan 160682231


def is_digits(sobj):
    # place code here - loop through each character in sobj 

    digits = {"0","1","2","3","4","5","6","7","8","9"}
    for string in sobj:
        if string not in digits:
            return False
    return True

    #Wrong codes !!!! if the first character is a digit, it returns True immediately — without checking the rest.
    # digits = {"0","1","2","3","4","5","6","7","8","9"}
    # for string in sobj:
    #     if string in digits:
    #         return True
    #     else:
    #         return False
    


if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')
