#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 10.12\n")
#
# Two words "interlock" if taking alternating letters from each forms a new 
# word. For example, "shoe" and "cold" interlock to form "schooled".
#
# Question 1
# 1. Write a program that finds all pairs of words that interlock.
#    Hint: don't enumerate all pairs!
#

#
# Question 2
# 2. Can you find any words that are three-way interlocked; that is, every third 
# letter forms a word, starting from the first, second or third?
#
import bisect

def word_list(file):
    fin = open(file)
    li = []
    
    for line in fin:
        word = line.strip()
        li.append(word)
    return li
    
def in_bisect(word_list, word):
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False
    return word_list[i] == word
    
def interlock(word_list):
    interlocker_list = []
    for word in word_list:
        if in_bisect(word_list, word[::2]) and in_bisect(word_list, word[1::2]):
            interlockers = (word[::2],word[1::2], word)
            interlocker_list.append(interlockers)
    return interlocker_list

def interlock_three(word_list):
    interlocker_list = []
    for word in word_list:
        if in_bisect(word_list, word[::3]) and in_bisect(word_list, word[1::3]) and in_bisect(word_list, word[2::3]):
            interlockers = (word[::3],word[1::3], word[2::3],  word)
            interlocker_list.append(interlockers)
    return interlocker_list
    
word_list = word_list('words.txt')
#print(interlock(word_list))
print(interlock_three(word_list))    