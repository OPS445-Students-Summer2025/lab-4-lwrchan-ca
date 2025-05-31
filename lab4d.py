#!/usr/bin/env python3
# The purpose of this script is to demonstrate creating and manipulating strings. 
# There will be four functions each will return a single string.
#Author Leung Wai Rene Chan 160682231

#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(String):
    # Place code here - refer to function specifics in section below
    substring = String[0:5]
    return substring

def last_seven(String):
#     # Place code here - refer to function specifics in section below
    substring = String[-7:]
    return substring

def middle_number(num):
#     # Place code here - refer to function specifics in section below
    String = str(num)
    substring = String[1:3]
    return substring


def first_three_last_three(X,Y):
#     # Place code here - refer to function specifics in section below
    substring = X[:3] + Y[-3:]
    return substring


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
