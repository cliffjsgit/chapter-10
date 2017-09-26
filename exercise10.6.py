#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 10.6\n")
#
# Question 1
# 1. Write a function called has_duplicates that takes a list and returns True
# if there is any element that appears more than once. It should not modify the
# original list.
#
def has_duplicates(li):
    dic = {}
    for item in li:
        if item in dic:
            return True
        else:
            dic[item] = 1

print(has_duplicates(['a','b','c']))