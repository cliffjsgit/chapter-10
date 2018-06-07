#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 10.12
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "version1" and "version2" should both return a list with all words
# in words.txt
# 
# Two words "interlock" if taking alternating letters from each forms a new 
# word. For example, "shoe" and "cold" interlock to form "schooled".
#
# Question 1
# 1. Write a function named "interlock" that finds all pairs of words that 
# interlock and returns a nested list in the following order: 
# [word[::2], word[1::2], word]
#    Hint: don't enumerate all pairs!
#
def interlock(word_list):
    return

#
# Question 2
# 2. Write a function named "three_way_interlock" that finds any words that are 
# three-way interlocked; that is, every third letter forms a word, starting from
# the first, second or third. Return a nested list in the following order: 
# [word[::3], word[1::3], word[2::3], word]
#
def three_way_interlock(word_list):
    return