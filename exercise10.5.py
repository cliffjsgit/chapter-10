#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 10.5\n")
#
# Question 1
# 1. Write a function called is_sorted that takes a list as a parameter and 
# returns True if the list is sorted in ascending order and False otherwise. 
# For example:
#
# >>> is_sorted([1, 2, 2])
# True
# >>> is_sorted(['b','a'])
# False
#
def is_sorted(li):
    return li == sorted(li)
    
print(is_sorted([1,3,7]))
