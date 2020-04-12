import sys

def simpleArraySum(n, ar):
    Sum = 0
    for num in ar:
        Sum += num
    return Sum

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)
