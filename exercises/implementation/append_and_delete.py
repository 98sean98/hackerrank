#!/bin/python

import sys

s = "abaaaa"
t = "abaaaaaaa"
k = 5
# s = raw_input().strip()
# t = raw_input().strip()
# k = int(raw_input().strip())
count = 0

# remove the first letter
def remove_first_letter(oldstr):
    if oldstr != "":
        return oldstr[1:]
    else:
        return oldstr

# return first letter
def first_letter(string):
    if string != "":
        return string[0]
    else:
        return ""


# length of s is longer than k
if len(s) > k:
    # compare the first letter of two strings and keep on removing until the first letters are different
    while first_letter(s) == first_letter(t):
        s = remove_first_letter(s)
        t = remove_first_letter(t)

    count = len(s) + len(t)

# length of s is equal to k
elif len(s) == k:
    count = 0

elif len(s) == len(t) and k >= len(s):
    count = k

elif len(s) < k:
    print 's < k'
    # compare the first letter of two strings and keep on removing until the first letters are different
    while first_letter(s) == first_letter(t) and (len(s) != 0 and len(t) != 0):
        print len(s)
        s = remove_first_letter(s)
        t = remove_first_letter(t)
    if(len(t) % 2) and k >= len(t):
        count = k
    # elif():


print count

if (count == k):
  print 'Yes'
else:
  print 'No'
