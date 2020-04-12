#!/bin/python

import sys

A,B,C,D = raw_input().strip().split(' ')
A,B,C,D = [int(A),int(B),int(C),int(D)]
ar = [A,B,C,D]

def small(ar):
    small = ar[0]
    for num in ar:
        if (num < small):
            small = num
    n = 0
    while n < len(ar):
        if(ar[n] == small):
            ar.pop(n)
            n = len(ar) + 1
        n += 1
    return small

arr = [small(ar), small(ar), small(ar), ar[0]]

W = 1
count = 0

while W <= arr[0]:
    X = W
    while X <= arr[1]:
        Y = X
        while Y <= arr[2]:
            Z = Y
            while Z <= arr[3]:
                if (W^X^Y^Z != 0):
                    count += 1
                Z += 1
            Y += 1
        X += 1
    W += 1

print count
