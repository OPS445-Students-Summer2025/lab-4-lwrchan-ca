#!/usr/bin/env python3
# The purpose of this script will be to improve the previous script to perform the same joins
# , matches, and diffs, but this time on lists.
#Author Leung Wai Rene Chan 160682231

def join_lists(l1, l2):
    # join_lists will return a list that contains every value from both l1 and l2
    return set(l1)| set(l2)   

def match_lists(l1, l2):
    # match_lists will return a list that contains all values found in both l1 and l2
    return set(l1) & set(l2)

def diff_lists(l1, l2):
    # diff_lists will return a list that contains all different values, which are not shared between the lists
    return set(l1) ^ set(l2)

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))

