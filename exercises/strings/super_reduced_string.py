#!/bin/python

import sys

def check_letters(s):
    char_temp = s[0]
    for char in s:
        if char == char_temp:
            return False
        char_temp = char
    return True


def super_reduced_string(s):
    i = 0
    while len(s) >= 1:
        if len(s) == 1:
            return s
        elif s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            i = 0
        else:
            i += 1
            if check_letters(s):
                return s
        print i, s
    if len(s) == 0:
        return 'Empty String'
    return s


s = raw_input().strip()
result = super_reduced_string(s)
print(result)
